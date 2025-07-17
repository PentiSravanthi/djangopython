from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hello_World(request):
    return HttpResponse('<h1>Hello from Django Application</h1>')