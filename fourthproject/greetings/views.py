from django.shortcuts import render
import datetime
from django.http import HttpResponse

# Create your views here.
def date_time_view(request):
    s = datetime.datetime.now()
    return HttpResponse('<h1>This Application Time'+str(s)+'</h1>')

