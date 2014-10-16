from django.shortcuts import render
from main.forms import URLForm

def index(request):
    if request.method == 'POST':
        url_form = URLForm(request.POST)
        if url_form.is_valid():
            cd = url_form.cleaned_data
            request.session['url'] = cd['url']
    else:
        url_form = URLForm(auto_id=False, label_suffix='')
    return render(request, 'main/index.html', {'url_form': url_form})
