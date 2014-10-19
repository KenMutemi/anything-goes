from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from main.forms import URLForm
from main.models import Summary
from lxml import html
import requests
import ast

def index(request):
    if request.method == 'POST':
        url_form = URLForm(request.POST)
        if url_form.is_valid():
            cd = url_form.cleaned_data
            url = cd['url']
            try:
                summary = Summary.objects.get(url=url)
                request.session['title'] = summary.title
                summary.paragraphs = ast.literal_eval(summary.paragraphs)
                request.session['paragraphs'] = summary.paragraphs
                summary.images = ast.literal_eval(summary.images)
                request.session['images'] = summary.images

            except (ValueError, Summary.DoesNotExist):
                response = requests.get(url)
                tree = html.fromstring(response.text)
                request.session['title'] = tree.xpath('//title/text()')[0].encode('utf-8').replace('\\xa0', ' ')
                request.session['paragraphs'] = tree.xpath('.//p/text()')
                request.session['images'] = tree.xpath('.//img/@src')

                Summary.objects.create(title=request.session['title'], paragraphs=request.session['paragraphs'],
                    images=request.session['images'], url=url)

            return HttpResponseRedirect(reverse("summary"))
    else:
        url_form = URLForm(auto_id=False, label_suffix='')
    return render(request, 'main/index.html', {'url_form': url_form})

def summary(request):
    return render(request, 'main/summary.html', {'title': request.session['title'],
        'paragraphs': request.session['paragraphs'], 'images': request.session['images']})
