from django.urls import path,include
from .views import cadastro,home,tela1,lista

urlpatterns = [
    path('cadastro/',cadastro),
    path('',home),
    path('tela/', tela1, name= "tela_url" ),
    path('listar/',lista,name = "lista_dos_dados")
]