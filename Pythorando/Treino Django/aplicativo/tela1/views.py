from django.shortcuts import render,HttpResponse
from aplicativo.settings import BASE_DIR


def tela1(request):
    print(BASE_DIR)
    return HttpResponse("Olá!")

def tela2(request):
    return render(request,'tela1.html')

def ficha_cadastro(request):
    return render(request,'ficha_cadastro.html')