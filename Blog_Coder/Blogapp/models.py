from urllib.parse import MAX_CACHE_SIZE
from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.


class Articulo(models.Model):
    titulo = models.CharField(max_length=128)
    sub_titulo = models.CharField(max_length=128, null=True, blank=True)
    fecha = models.DateField()
    autor = models.CharField(max_length=128)
    email_autor = models.EmailField()
    cuerpo = RichTextField(max_length=5000, blank=True, null=True,)
    imagen = models.ImageField(upload_to='imagenes', null=True, blank=True)

    def __str__(self):
        return f'{self.titulo}'
