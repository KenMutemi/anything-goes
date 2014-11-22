from django import forms

class URLForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={'id': 'input-url', 'class' : 'form-control url-form-control', 
        'placeholder': 'Enter a URL here', 'type':'text'}))
