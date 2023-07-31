from django.db import models
from django.contrib.auth.models import User

class Evento(models.Model):
    titulo = models.CharField(
        verbose_name = "Titulo",
        max_length = 100
    )
    descricao = models.TextField(
        verbose_name = "Descrição",
        max_length = 100,
        blank = True,
        null = True
    )
    numero = models.IntegerField(
        verbose_name = "numero"
    )
    data_evento = models.DateField(
        verbose_name = "Data do Evento"
    )
    data_criacao = models.DateField(
        verbose_name = "Data da criacao",
        auto_now = True
    )
    usuario = models.ForeignKey(
        User,
        on_delete = models.PROTECT,
        blank = False,
        null = False
    )
    class Meta:
        db_table = "evento" # fixa o nome da Mesa
        unique_together = ['titulo','data_criacao'] # Manter só uma tabela com os determinados tipos de dados

    def __str__(self):
        return self.titulo
    
    def get_data_evento(self):
        return self.data_evento.strftime('%d/%m/%Y')
