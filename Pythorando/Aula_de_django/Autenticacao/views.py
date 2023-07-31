from django.shortcuts import render,HttpResponse
# from django.http import HttpResponse

def cadastro(request):
    dicionario = [{"name" : "Breno",
                  "idade" : 21,
                  "profissão" : "Pescador Profissional"},
                  {"name" : "Lucas",
                  "idade" : 25,
                  "profissão" : "Vendedor Profissional"}]
    
    return render(request,'index.html',{"dicionario":dicionario})  #aqui no caso o dicionario trabalha se auto referenciando,igual um (self ou cls)

def home(request):
    return render(request,'entrada.html')


