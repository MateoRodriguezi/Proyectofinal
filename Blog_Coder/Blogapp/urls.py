from unicodedata import name
from django.urls import path
from Blogapp.models import Articulo
from Blogapp import views

urlpatterns = [
    path('', views.home, name='Inicio'),
    path('pages/', views.ArticuloListView.as_view(), name='Articulos'),
    path('about/', views.about, name='Acerca de'),
    path(r'^(?P<pk>/d+)$', views.ArticuloDetailView.as_view(), name="Detail"),
    path(r'^nuevo$', views.ArticuloCreateView.as_view(model= Articulo, success_url="/blog-viajes/pages"), name="New"),
    path(r'^editar/(?P<pk>/d+)$', views.ArticuloUpdateView.as_view(model= Articulo, success_url="/blog-viajes/pages"), name="Edit"),
    path(r'^borrar/(?P<pk>/d+)$', views.ArticuloDeleteView.as_view(model= Articulo, success_url="/blog-viajes/pages"), name="Delete"),
]