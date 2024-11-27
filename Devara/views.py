from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def NTR(request):
    return HttpResponse('<h1>Devara is NTR Movie</h1>')

def NTR2(request):
    return HttpResponse('<h1>Part2 is there in Devara</h1>')