from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Allu(request):
    return HttpResponse('<h1>Upcommimg Movie is This one</h1>')

def Arjun(request):
    return HttpResponse('<h1>This one is part2 of AA</h1>')