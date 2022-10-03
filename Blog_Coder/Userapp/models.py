from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User


# Create your models here.


class Avatar(models.Model):
    User = models.ForeignKey(User, on_delete=models.CASCADE)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo}'

class Perfil(models.Model):
    # Vinculo con el usuario
    user = models.OneToOneField(User, on_delete = models.CASCADE, null = True)
    # Campos a modificar
    nombre = models.CharField(max_length=128, blank=True, null=True)
    fecha_nacimiento = models.DateField(blank = True, null=True)
    domicilio = models.CharField(max_length=128, blank = True, null = True)
    telefono = models.IntegerField(blank = True, null = True)
    bio = models.TextField(max_length=600, blank = True, null = True)
    link_web = models.URLField(max_length=128, blank = True, null = True)
