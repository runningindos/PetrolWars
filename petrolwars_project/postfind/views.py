from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return HttpResponse('<h1>Postfind Home</h1>')

def search(request):
    return HttpResponse('<h1>Postfind-Search</h1>')

def share(request):
    return HttpResponse('<h1>Postfind-Share</h1>')