from unicodedata import name
from django.urls import path
from Blogapp.models import Articulo
from Blogapp import views

urlpatterns = [
    path('pages/', views.ListaArticulos.as_view(), name='Articulos'),
    path('', views.home, name='Inicio'),
    path('about/', views.about, name='Acerca de'),
    path(r'^(?P<pk>/d+)$', views.DetalleArticulos.as_view(), name="Detail"),
    path(r'^nuevo$', views.CrearArticulo.as_view(model= Articulo, success_url="/blog-viajes/pages"), name="New"),
    path(r'^editar/(?P<pk>/d+)$', views.EditarArticulo.as_view(model= Articulo, success_url="/blog-viajes/pages"), name="Edit"),
    path(r'^borrar/(?P<pk>/d+)$', views.EliminarArticulo.as_view(model= Articulo, success_url="/blog-viajes/pages"), name="Delete"),
]