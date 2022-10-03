from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from Userapp.forms import UserRegisterForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.contrib.auth.models import User
from Userapp.forms import UserEditForm
from Userapp.models import Perfil
from django.urls import reverse_lazy




def login_request(request):

    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contra = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contra)

            if user is not None:
                login(request, user)

                return render(request, 'Blogapp/home.html', {"mensaje": f"Bienvenido {usuario}"})
            else:
                return render(request, 'Blogapp/home.html', {"mensaje": f"Error, datos incorrectos"})

        else:
            return render(request, 'Blogapp/home.html', {"mensaje": f"Error, formulario erroneo"})

    form = AuthenticationForm()

    return render(request, 'Userapp/login.html', {'form': form})


def register_request(request):

    if request.method == "POST":

        form = UserRegisterForm(request.POST)

        if form.is_valid():

            username = form.cleaned_data['username']
            form.save()
            return render(request, 'Blogapp/home.html', {"mensaje": "Usuario creado exitosamente"})

    else:
        form = UserRegisterForm()

    return render(request, 'Userapp/registro.html', {"form": form})


class CustomLogoutView(LogoutView):
    template_name = 'Userapp/logout.html'

@login_required
def EditarPerfil(request):

    usuario = request.user

    if request.method == 'POST':
        miFormulario = UserEditForm(request.POST)
        if miFormulario.is_valid():
            
            informacion = miFormulario.cleaned_data

            usuario.email = informacion['email']
            usuario.password1 = informacion['password1']
            usuario.password2 = informacion['password2']
            usuario.save()

            return render(request, "Blogapp/home.html", {"mensaje": "La información se ha modificado con éxito"})
    
    else: 
        miFormulario = UserEditForm(initial={'email':usuario.email})

    return render(request, "UserApp/editar_perfil.html", {"miFormulario":miFormulario, "usuario":usuario})

class PerfilUpdate(LoginRequiredMixin, UpdateView):
    model = Perfil
    fields = ['nombre', 'domicilio', 'telefono', 'bio', 'link_web']
    template_name = 'Userapp/perfil_form.html'
    success_url = reverse_lazy('Inicio')

    def get_object(self):
        profile, created = Perfil.objects.get_or_create(user=self.request.user)
        return profile
