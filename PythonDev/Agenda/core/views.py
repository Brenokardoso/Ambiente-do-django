from django.shortcuts import render,HttpResponse,redirect
from core.models import Evento


def index(request):
    return redirect('/agenda/')

def lista_eventos(request):
    usuario = request.user
    eventos = Evento.objects.filter(usuario = usuario)
    dados = {'eventos':eventos}
    return render(request,'agenda.html',dados)

def teste(request):
    return HttpResponse("OK")