# Generated by Django 4.2.3 on 2023-08-18 12:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tela1', '0004_cargo'),
    ]

    operations = [
        migrations.AddField(
            model_name='pessoa',
            name='cargo',
            field=models.ForeignKey(default=2, on_delete=django.db.models.deletion.CASCADE, to='tela1.cargo'),
            preserve_default=False,
        ),
    ]