from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Kartikeya(request):
    return HttpResponse('<h1>It is a Military Movie</h1>')

def Kartikeya2(request):
    return HttpResponse('<h1>It is also a Love Story</h1>')