from django.shortcuts import render
from django.http import HttpResponse
from .models import Formulario

def tela1(request):
    return render(request,'tela1.html')


def form(request):

    # nome = request.POST.get('nome')
    # idade = request.POST.get('idade')
    # email = request.POST.get('email')
    # endereço = request.POST.get('email')


    formulario = Formulario()
    formulario.name = request.POST.get('name')
    formulario.idade = request.POST.get('idade')
    formulario.email = request.POST.get('email')
    formulario.endereço = request.POST.get('endereço')
    formulario.save()
    return render(request,'formulario.html',{'formulario':formulario})

def view_form_data(request):
    os_dados = Formulario.objects.all()
    return render(request,'all_data.html',{'os_dados':os_dados})