# Generated by Django 4.1.1 on 2022-10-03 02:45

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Blogapp', '0003_alter_articulo_cuerpo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articulo',
            name='cuerpo',
            field=ckeditor.fields.RichTextField(blank=True, max_length=5000, null=True),
        ),
    ]