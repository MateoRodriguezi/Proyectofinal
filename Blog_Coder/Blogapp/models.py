from urllib.parse import MAX_CACHE_SIZE
from django.db import models

# Create your models here.

class Articulo(models.Model):
    titulo = models.CharField(max_length=128)
    fecha = models.DateField()
    autor = models.CharField(max_length=128)
    email_autor = models.EmailField()
    
    
    