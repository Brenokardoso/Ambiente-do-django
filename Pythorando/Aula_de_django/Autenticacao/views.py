from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from Aula_de_django.settings import BASE_DIR
from .models import Pessoa
import json
import random




def cadastro(request):    
    nome = request.GET.get('nome')
    sobrenome = request.GET.get('sobrenome')
    idade = request.GET.get('idade')
    return render(request,'cadastro/index.html',{'nome':nome,'sobrenome':sobrenome,'idade':idade})  #aqui no caso o dicionario trabalha se auto referenciando,igual um (self ou cls)


def home(request):
    return render(request,'home/entrada.html')


def tela1(request):   
    pessoa = Pessoa()
    pessoa.nome = request.POST.get('nome')
    pessoa.email = request.POST.get('email')
    pessoa.senha = request.POST.get('senha')
    pessoa.id = random.randint(1,999)
    pessoa.save()
    return render(request,'telas/telas1.html',{'pessoa': pessoa})

def lista(request):
    lista_pessoas = Pessoa.objects.all()
    print(lista_pessoas)
    return render(request,'telas/listar.html',{'listar': lista_pessoas})
