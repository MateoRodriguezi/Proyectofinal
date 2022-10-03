# Proyectofinal

LINK A VIDEO DEMO: https://drive.google.com/file/d/18yjFSfc94NA_QY90hwztXlYS7q6t9bqL/view?usp=sharing (Descargar y ver preferentemente con QuickTime Player.

El proyecto es un blog construido sobre Django con patrón MVT. Tambien se utilizo:

Python
Django 
Pillow
Ckeditor 

Pre-requisitos:

Para poder ejecutar el proyecto, es necesario la instalación del archivo requirements.txt el cual contiene:

asgiref==3.5.2
autopep8==1.7.0
backports.zoneinfo==0.2.1
Django==4.1.1
django-ckeditor==6.5.1
django-js-asset==2.0.0
Pillow==9.2.0
pycodestyle==2.9.1
sqlparse==0.4.2
toml==0.10.2

Usuarios disponibles:
Superusuario:

blogapp -> Pass: blogapp1234

Usuarios dados de Alta:

cachulito -> Pass: uruguay1234
herni1910 -> Pass: holahernan1234

Se realizaron 3 pruebas unitarias:
        # Test 1: Verifica si el max_lenght del campo cuerpo coincide con el max_lenght del modelo
        # Test 2: Verifica si el def __str__(self) del modelo coincide con el titulo
        # Test 3: Verifica si el max_lenght del campo autor coincide con el max_lenght del modelo

para correrlas se debe escribir en la terminal el comando python manage.py test.

Autores:

Mateo Rodriguez Pintos y Macarena Gomez Pujal

Ambos trabajamos de forma equitativa en el proyecto, realizando el maquetado y dando las funcionalidades en conjunto. 
Tambien buscamos y discutimos soluciones a los bugs que se nos presentaron.


ACLARACIONES:

En el punto 4 de la rubrica elegimos la opcion de fotos de articulos, siendo que solamente los admin puedan crear, editar o borrar fotos desde el
admin de Django.
