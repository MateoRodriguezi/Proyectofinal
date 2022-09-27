from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from http.client import HTTPResponse
from typing import Dict
from urllib.request import HTTPRedirectHandler
from django.shortcuts import render
from django.http import HttpResponse
from Blogapp.models import *

# Create your views here.

def home(request):
    return render (request, "Blogapp/home.html")

def about(request):
    return render (request, "Blogapp/about.html")

def pages(request):
    return render (request, "Blogapp/pages.html")

class ArticuloListView(ListView):
    model = Articulo
    template_name = 'Blogapp/pages.html'

class ArticuloDetailView(DetailView):
    model = Articulo
    template_name = 'Blogapp/page_id.html'

class ArticuloCreateView(CreateView):
    model = Articulo
    succes_url = "/Blogapp/pages"
    fields = ['titulo', 'sub_titulo', 'fecha', 'autor', 'email_autor', 'cuerpo', 'imagen']

class ArticuloUpdateView(UpdateView):
    model = Articulo
    succes_url = "/Blogapp/pages"
    fields = ['titulo', 'sub_titulo', 'fecha', 'autor', 'email_autor', 'cuerpo', 'imagen']

class ArticuloDeleteView(DeleteView):
    model = Articulo
    succes_url = "/Blogapp/pages"