# Generated by Django 2.0.2 on 2020-04-08 23:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0007_remove_noticia_seccion'),
    ]

    operations = [
        migrations.DeleteModel(
            name='noticia',
        ),
    ]