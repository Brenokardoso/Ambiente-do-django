from django.shortcuts import render,HttpResponse
from aplicativo.settings import BASE_DIR 
from .models import Cadastro


def tela1(request):
    print(BASE_DIR)
    return HttpResponse("Olá!")

def tela2(request):
    return render(request,'tela1.html')

def ficha_cadastro(request):

    cadastro = Cadastro()
    cadastro.nome = request.POST.get('nome')
    cadastro.idade = request.POST.get('idade')
    cadastro.cpf = request.POST.get('cpf')
    cadastro.altura = request.POST.get('altura')
    cadastro.peso = request.POST.get('peso')
    cadastro.sexo = request.POST.get('sexo')
    cadastro.save()
    dados = Cadastro.objects.all()
    return render(request,'ficha_cadastro.html',{'cadastro':cadastro,'dados':dados})

def chave(request):
    nome = request.POST.get('nome')
    idade = request.POST.get('idade')
    return render(request,'chave.html',{'nome' : nome , 'idade' : idade})  