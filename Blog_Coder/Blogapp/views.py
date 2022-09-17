from django.shortcuts import render
from http.client import HTTPResponse
from typing import Dict
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from Blogapp.models import *

# Create your views here.

def home(request):
    return render (request)

def about(request):
    return render (request, )

def pages(request):
    return render (request,)