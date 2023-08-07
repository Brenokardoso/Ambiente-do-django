from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from Aula_de_django.settings import BASE_DIR
import json


def cadastro(request):    
    nome = request.GET.get('nome')
    sobrenome = request.GET.get('sobrenome')
    idade = request.GET.get('idade')
    return render(request,'cadastro/index.html',{'nome':nome,'sobrenome':sobrenome,'idade':idade})  #aqui no caso o dicionario trabalha se auto referenciando,igual um (self ou cls)


def home(request):
    return render(request,'home/entrada.html')


def tela1(request):
    # nome = request.GET.get('nome')
    # email = request.GET.get('email')

    nome = request.POST.get('nome')
    email = request.POST.get('email')

    return render(request,'telas/telas1.html',{'nome':nome,'email':email})

