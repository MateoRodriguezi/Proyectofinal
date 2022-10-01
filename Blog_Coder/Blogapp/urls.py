from unicodedata import name
from django.urls import path
from Blogapp.models import Articulo
from Blogapp import views

urlpatterns = [
    path('', views.home, name='Inicio'),
    path('pages', views.ArticuloListView.as_view(), name='Articulos'),
    path('about/', views.about, name='Acerca de'),
    path('pages/<int:pk>', views.ArticuloDetailView.as_view(), name="Detail"),
    path(r'^nuevo$', views.ArticuloCreateView.as_view(model=Articulo, success_url="/blog-viajes/pages/"), name="New"),
    path('editar/<int:pk>/', views.ArticuloUpdateView.as_view(model=Articulo,success_url="/blog-viajes/pages/"), name="Edit"),
    path('eliminar/<int:pk>/', views.ArticuloDeleteView.as_view(model=Articulo,success_url="/blog-viajes/pages/"), name="Delete"),
]
