from datetime import datetime

from django.test import TestCase
from Blogapp.models import Articulo
from django.utils.crypto import get_random_string
import tempfile

class ArticuloTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):      
        title_test = get_random_string(length=50)
        subtitle_test = get_random_string(length=100)
        content_test = get_random_string(length=2000)
        author_test = get_random_string(length=60)
        date_test = datetime.now()

        # Creación de un articulo
        Articulo.objects.create(titulo=title_test, sub_titulo=subtitle_test, cuerpo=content_test, autor=author_test, fecha=date_test)
        

    def test_cuerpo_max_length(self):
        # Test 1: Verifica si el max_lenght del campo cuerpo coincide con el max_lenght del modelo
        articulo_test = Articulo.objects.get(id=1)
        max_length = articulo_test._meta.get_field('cuerpo').max_length
        self.assertEqual(max_length, 128)

    def test_object_name_is_title(self):
        # Test 2: Verifica si el def __str__(self) del modelo coincide con el titulo
        articulo_test = Articulo.objects.get(id=1)
        expected_object_name = f'{articulo_test.titulo}'
        self.assertEqual(str(articulo_test), expected_object_name)

    def test_autor_max_length(self):
        # Test 3: Verifica si el max_lenght del campo autor coincide con el max_lenght del modelo
        articulo_test = Articulo.objects.get(id=1)
        max_length = articulo_test._meta.get_field('autor').max_length
        self.assertEqual(max_length, 128)