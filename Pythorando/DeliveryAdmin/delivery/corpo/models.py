from django.db import models



class Cargo(models.Model):
    nome = models.CharField(
        verbose_name = "Cargo",
        max_length = 100,
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nome

class Pessoa(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 200,
        null = True,
        blank = True
    )
    email = models.EmailField(
        verbose_name = "Email",
        null = True,
        blank = True
    )
    senha = models.CharField(
        verbose_name = "Senha",
        max_length = 200,
        null = True,
        blank = True
    )
    cargo = models.ForeignKey(
        Cargo,
        on_delete = models.DO_NOTHING
    )

    def __str__(self):
        return self.nome

class Pedido(models.Model):
    nome = models.CharField(
        verbose_name = "Nome do Pedido",
        max_length = 100,
        null = True,
        blank = True
    )
    quantidade = models.PositiveIntegerField(
        verbose_name = "Quantiade",
        null = True,
        blank = True

    )
    descricao = models.TextField(
        verbose_name = "Descrição",
        null = True,
        blank = True  
    )
    pessoa = models.ForeignKey(
        Pessoa,
        on_delete = models.DO_NOTHING
    )
    horario = models.TimeField(
        verbose_name = "Tempo estimado para entrega",
        null = True,
        blank = True,
    )
    
    def __str__(self):
        return f"{self.nome}"
    
    def __str__(self):
        return self.horario.strftime("%H:%M")