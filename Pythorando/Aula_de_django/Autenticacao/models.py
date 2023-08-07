from django.db import models

class Pessoa(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 100,
        blank = True,
        null = True,
    )
    email = models.EmailField(
        verbose_name = "Email",
        blank = True,
        null = True 
    )
    senha = models.CharField(
        verbose_name = "Senha",
        max_length = 100,
        blank =False,
        null = False,
        
    )