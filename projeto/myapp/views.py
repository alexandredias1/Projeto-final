from django.shortcuts import render

def home(request):

    return render(request, 'metafit/home.html')