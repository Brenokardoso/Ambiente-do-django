from django.shortcuts import render,HttpResponse
from django.http import HttpResponse
from Aula_de_django.settings import BASE_DIR


def cadastro(request):    
    return render(request,'cadastro/index.html')  #aqui no caso o dicionario trabalha se auto referenciando,igual um (self ou cls)


def home(request):
    return render(request,'home/entrada.html')


