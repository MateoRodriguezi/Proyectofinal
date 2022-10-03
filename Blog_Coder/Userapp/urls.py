from unicodedata import name
from django.urls import path
from Userapp import views
from Userapp.views import PerfilUpdate

urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('signup/', views.register_request, name='Register'),
    path('logout/', views.CustomLogoutView.as_view(), name='Logout'),
    path('editar-perfil', views.EditarPerfil, name='Editar Perfil'),
    path('profile/', PerfilUpdate.as_view(), name = 'Perfil'),
]
