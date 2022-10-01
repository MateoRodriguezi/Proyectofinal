from django.shortcuts import render, redirect, reverse
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.views.generic import CreateView, UpdateView, DeleteView, ListView
from django.contrib.auth.mixins import LoginRequiredMixin
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

class ArticuloCreateView(CreateView, LoginRequiredMixin):
    model = Articulo
    fields = ['titulo', 'sub_titulo', 'fecha', 'autor', 'email_autor', 'cuerpo']
    succes_url = reverse_lazy('Inicio')

class ArticuloUpdateView(UpdateView, LoginRequiredMixin):
    model = Articulo
    succes_url = reverse_lazy('Inicio')
    fields = ['titulo', 'sub_titulo', 'fecha', 'autor', 'email_autor', 'cuerpo']

class ArticuloDeleteView(DeleteView, LoginRequiredMixin):
    model = Articulo
    succes_url = reverse_lazy('Inicio')
