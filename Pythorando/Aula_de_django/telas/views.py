from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario

def tela1(request):
    return render(request,'tela1.html')


def form(request):
    formulario = Formulario()
    formulario.name = request.POST.get('name')
    formulario.idade = request.POST.get('idade')
    formulario.email = request.POST.get('email')
    formulario.endereço = request.POST.get('endereço')
    formulario.save()
    return render(request,'formulario.html',{'formulario':formulario})

def view_form_data(request):
    # os_dados = Formulario.objects.all()
    os_dados = Formulario.objects.filter(name = None).filter(idade = 12).filter(endereço ='sla man') #Filtro de objetos usando o operador logico and ('e')
    return render(request,'all_data.html',{'os_dados':os_dados})

