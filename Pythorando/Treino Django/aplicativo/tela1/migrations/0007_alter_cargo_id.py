# Generated by Django 4.2.3 on 2023-08-18 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tela1', '0006_alter_pessoa_cargo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cargo',
            name='id',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]