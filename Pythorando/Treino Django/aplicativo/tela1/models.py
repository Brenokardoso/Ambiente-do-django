from django.db import models

class Cadastro(models.Model): 
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 100,
        null = True,
        blank = True
    )
    idade = models.PositiveIntegerField(
        verbose_name = "idade",
        null = True,
        blank = True
    )
    cpf = models.IntegerField(
        verbose_name = "CPF",
        null = True,
        blank = True
    )
    altura = models.FloatField(
        verbose_name = "Altura",
        null = True,
        blank = True
    )
    peso = models.FloatField(
        verbose_name = "Peso",
        null= True,
        blank = True,
    )
    sexo = models.CharField(
        verbose_name = 'Sexo',
        max_length = 100,
        null= True,
        blank= True
    )

    def __repr__(self):
        return self.nome
    