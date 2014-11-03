from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.contrib import messages
from main.forms import URLForm
from main.models import Summary
from django.contrib.auth.decorators import login_required
from lxml import html
import requests
from requests.exceptions import ConnectionError
from urlparse import urlparse
import ast

def index(request):
    if request.method == 'POST':
        url_form = URLForm(request.POST)
        if url_form.is_valid():
            cd = url_form.cleaned_data
            url = cd['url']
            request.session['url'] = url
            try:
                summary = Summary.objects.get(url=url)
                request.session['title'] = summary.title
                summary.paragraphs = ast.literal_eval(summary.paragraphs)
                request.session['paragraphs'] = summary.paragraphs
                summary.images = ast.literal_eval(summary.images)
                request.session['images'] = summary.images
                if request.user.is_authenticated():
                    try:
                        Summary.objects.get(user=request.user.id, url=url)
                    except (ValueError, Summary.DoesNotExist):
                        summary.user.add(request.user.id)
                        summary.save()

            except (ValueError, Summary.DoesNotExist):
                hdr = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
                       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
                       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
                       'Accept-Encoding': 'none',
                       'Connection': 'keep-alive'}
                try:
                    response = requests.get(url, headers=hdr)
                    parsed_uri = urlparse(url)
                    tree = html.fromstring(response.content)
                    try:
                        request.session['title'] = tree.xpath('//title/text()')[0].encode('utf-8').replace('\\xa0', ' ')
                    except IndexError:
                        request.session['title'] = '[title not available]'
                    paragraphs = tree.xpath('.//p')
                    request.session['paragraphs'] = [paragraph.text_content() for paragraph in paragraphs]
                    domain = '{uri.scheme}://{uri.netloc}/'.format(uri=parsed_uri)
                    images = tree.xpath('.//img/@src')
                    request.session['images'] = [domain+image if not image.startswith(domain)
                            and not image.startswith('http') else image for image in images]
                    try:
                        summary = Summary.objects.create(title=request.session['title'], paragraphs=request.session['paragraphs'],
                                images=request.session['images'], url=url)
                        if request.user.is_authenticated():
                            summary.user.add(request.user.id)
                            summary.save()
                    except Exception:
                        pass
                except ConnectionError:
                    request.session['title'] = 'Oops! Sorry could not connect to that url.'
                    messages.add_message(request, messages.ERROR, 'Oops! Sorry could not connect to that url.')

            return HttpResponseRedirect(reverse("summary"))
    else:
        url_form = URLForm(auto_id=False, label_suffix='')
    return render(request, 'main/index.html', {'url_form': url_form, 'title': 'Home'})

def summary(request):
    url_form = URLForm(auto_id=False, label_suffix='')
    return render(request, 'main/summary.html', {'url_form': url_form, 'title': request.session['title'],
        'paragraphs': request.session['paragraphs'], 'images': request.session['images'],
        'url': request.session['url'], 'request': request})
@login_required(login_url='/')
def summaries(request):
    url_form = URLForm(auto_id=False, label_suffix='')
    if request.method == 'POST':
        request.POST.get('delete')
        summary = Summary.objects.get(url=request.POST.get("url", ""))
        summary.user.remove(request.user.id)
    return render(request, 'main/summaries.html', {'url_form': url_form, 'summaries': Summary.objects.filter(user=request.user.id)})
