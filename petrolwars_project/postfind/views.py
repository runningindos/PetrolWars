from django.shortcuts import render
from django.http import HttpResponse
from .models import Station


# Create your views here.

def home(request):
    return HttpResponse('<h1>Postfind Home</h1>')

def search(request):
    context = {
        'station': Station.objects.all()
    }
    return render(request, 'postfind/search.html', context)

def share(request):
    return HttpResponse('<h1>Postfind-Share</h1>')

