from django.db import models
# from django.db.models.fields import CharField



class Cargo(models.Model):
    name = models.CharField(
        verbose_name = "Nome",
        max_length = 200,
        default = "Zé Roberto"
    )
    def __str__(self):
        return self.name

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
    cargo = models.ForeignKey(
        Cargo,
        on_delete = models.DO_NOTHING,
        verbose_name = "Fcargo"
    )
    