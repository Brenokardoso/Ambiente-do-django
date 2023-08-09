from django.db import models

class Formulario(models.Model):
    name = models.CharField(
        max_length = 200,
        verbose_name = "Nome",
        null = True,
        blank = True,
    )
    idade = models.PositiveIntegerField(
        verbose_name = "Idade",
        null = True,
        blank = True,
        default = 0,
    )
    email = models.EmailField(
        verbose_name = "Email",
        max_length = 200,
        null = True,
        blank = True,
    )
    endereço = models.TextField(
        verbose_name = "Endereço",
        null = True,
        blank = True,
    )