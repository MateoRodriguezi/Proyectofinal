from unicodedata import name
from django.urls import path
from Userapp import views


urlpatterns = [
    path('login/', views.login_request, name='Login'),
    path('signup/', views.register_request, name='Register'),
    path('logout/', views.CustomLogoutView.as_view(), name='Logout'),
]
