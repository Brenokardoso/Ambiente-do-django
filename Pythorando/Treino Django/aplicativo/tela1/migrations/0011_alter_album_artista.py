# Generated by Django 4.2.3 on 2023-08-18 17:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tela1', '0010_alter_album_artista'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='artista',
            field=models.ManyToManyField(to='tela1.artista'),
        ),
    ]
