from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from main.forms import URLForm
from lxml import html
import requests

def index(request):
    if request.method == 'POST':
        url_form = URLForm(request.POST)
        if url_form.is_valid():
            cd = url_form.cleaned_data
            url = cd['url']
            response = requests.get(url)
            tree = html.fromstring(response.text)
            request.session['title'] = str(tree.xpath('//title/text()')[0]).replace('\\xa0', ' ')

            return HttpResponseRedirect(reverse("summary"))
    else:
        url_form = URLForm(auto_id=False, label_suffix='')
    return render(request, 'main/index.html', {'url_form': url_form})

def summary(request):
    return render(request, 'main/summary.html', {'title': request.session['title']})
