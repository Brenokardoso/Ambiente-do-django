from django.shortcuts import render
from django.http import HttpResponse
from django.db.models import Q
from .models import Formulario,Cargos
import random

def tela1(request):
    return render(request,'tela1.html')


def form(request):
    formulario = Formulario()
    formulario.name = request.POST.get('name')
    formulario.idade = request.POST.get('idade')
    formulario.email = request.POST.get('email')
    formulario.endereço = request.POST.get('endereço')

    # cargo = Cargos.objects.create(pk = 5,nome = "None")
    nome = request.POST.get('nome')
    # formulario.cargo = cargo
    formulario.save()
    return render(request,'formulario.html',{'formulario':formulario,'nome':nome})

def view_form_data(request):
    if len(request.GET) != 0:
        nome = request.GET.get('name')
        idade = request.GET.get('idade')
        email = request.GET.get('email')
        endereço = request.GET.get('endereço')

        cargo = Cargos.objects.filter(nome = 'DEV')[0]
        print(cargo.nome)
        
        pessoaex = Formulario(
            nome = nome,idade = idade, email = email,endereço = endereço
        )

    os_dados = Formulario.objects.all()
    # os_dados = Formulario.objects.filter(name = None).filter(idade = 12).filter(endereço ='sla man') #Filtro de objetos usando o operador logico and ('e')
    # os_dados = Formulario.objects.filter(name = None) | Formulario.objects.filter(idade = 12) #Filtro usando o operador logico and
    # os_dados = Formulario.objects.filter(Q(name = None)|Q(idade = 12))  # Filtro usnado a classe Q do django.db.models
    # os_dados = Formulario.objects.filter(Q(name = 'breno')|Q(idade = 12)).exclude(name = None) # Aqui vemos como o exclude funciona agindo em cima dos None's objects
    # pessoa = os_dados.filter(idade = 444) # Aqui temos o método de deleção de um objeto com seus métodos e atributos
    # pessoa.delete()

    # os_cargos = Cargo()
    # os_cargos.name = "ADM"
    # os_cargos.save()
    return render(request,'all_data.html',{'os_dados':os_dados,'pessoa':pessoa})
    




