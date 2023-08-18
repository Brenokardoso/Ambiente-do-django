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
    

class Cargo(models.Model):
    id = models.IntegerField(
       primary_key= True
    )
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 100,
        null = True,
        blank = True,
    )
    
    def __str__(self):
        return self.nome


class Pessoa(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 100,
        null = True,
        blank = True 
    )
    email = models.EmailField(
        verbose_name = "Email",
        null = True,
        blank = True
    )
    senha = models.CharField(
        verbose_name = "senha",
        max_length = 200,
        null = True,
        blank = True
    )
    cargo = models.ForeignKey(
        Cargo,
        on_delete=models.CASCADE,
        null = True,
        blank = True 
    )

    def __str__(self):
        return self.nome
    

class Artista(models.Model):
    nome = models.CharField(
        verbose_name = "Nome",
        max_length = 50 ,
        null = True,
        blank = True
    )
    genero = models.CharField(
        verbose_name = "genero",
        max_length = 50,
        null = True,
        blank = True
    )
    data_de_nascimento = models.DateField(
        verbose_name = "Data",
        null = True,
        blank = True
    )
    local_nascimento = models.TextField(
        verbose_name = "Naturalidade",
        null = True,
        blank = True
    )

    def __str__(self):
        return self.nome


class Album(models.Model):
    titulo = models.CharField(
        max_length = 200,
        verbose_name = "Titulo",
        null = True,
        blank = True 
    )
    ano_lancamento = models.DateField(
        verbose_name = "Ano de lançamento",
        null = True,
        blank = True,
    )
    genero = models.CharField(
        verbose_name = "genero",
        max_length = 200,
        null = True,
        blank = True,
    )
    artista = models.ManyToManyField(
        Artista,
    )
    numero_de_faixas = models.PositiveIntegerField(
        verbose_name = "numero de faixas",
        null = True,
        blank = True,
    )
    tempo_de_musica = models.FloatField(
        verbose_name = "Tempo de Musica",
        blank = True,
        null = True 
    )

    def __str__(self):
        self.titulo

    
        
