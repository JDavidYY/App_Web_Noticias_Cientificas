# Generated by Django 2.0.2 on 2020-04-06 21:29

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_auto_20200406_1249'),
    ]

    operations = [
        migrations.RenameField(
            model_name='noticia',
            old_name='year_in_school',
            new_name='seccion',
        ),
    ]