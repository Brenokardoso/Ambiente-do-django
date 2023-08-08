from django.shortcuts import render
from django.http import HttpResponse

def tela1(request):
    return render(request,'tela1.html')


def form(request):
    return render(request,'formulario.html')