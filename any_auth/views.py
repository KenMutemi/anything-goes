from django.shortcuts import render

def home(request):
    return render(request, 'any_auth/index.html', {'request': request, 'user': request.user})
