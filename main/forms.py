from django import forms

class URLForm(forms.Form):
    url = forms.URLField(widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder': 'Enter a url here', 'type':'url'}))
