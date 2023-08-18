from django.shortcuts import render,HttpResponse
from aplicativo.settings import BASE_DIR 
from .models import Cadastro,Pessoa,Cargo,Artista,Album


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
    pessoa = Pessoa()
    trabalho = Cargo()
    pessoa.nome = request.POST.get('nome')
    pessoa.email = request.POST.get('email')
    pessoa.senha = request.POST.get('senha')
    pessoa.cargo_id = request.POST.get('cargo_id')
    trabalho.id = request.POST.get('id')
    trabalho.nome = request.POST.get('nome_trabalho')
    pessoa.save()
    trabalho.save()
    return render(request,'chave.html',{'pessoa':pessoa,'trabalho':trabalho})  

def  listar_chave(request):
    chaves = Pessoa.objects.all()
    return render(request,'listar_chave.html',{'chaves':chaves})

def manytomany(request):
    pessoa = Pessoa.objects.all()
    
    return render(request,'manytomany.html',{'pessoa':pessoa})

def listar_dinamico(request,id):
    pessoa = Pessoa.objects.filter(id = id)
    return render(request,'listar_chave.html',{'pessoa':pessoa})

def home(request):
    return render(request,'home.html')