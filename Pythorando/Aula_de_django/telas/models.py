from django.db import models
# from django.db.models.fields import CharField


class Cargos(models.Model):
    nome = models.CharField(
        verbose_name = "nome",
        max_length = 100,
        null = True,
        blank = True,
    )


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
    cargos = models.ForeignKey(
        Cargos,
        on_delete = models.DO_NOTHING,
        null = True,
        blank = True
    )

    