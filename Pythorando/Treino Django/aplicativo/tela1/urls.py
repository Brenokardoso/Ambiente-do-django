from django.contrib import admin
from django.urls import path,include
from .views import tela1,tela2,ficha_cadastro,chave,listar_chave,manytomany,listar_dinamico,home


urlpatterns = [
    path('',home),
    path('1/',tela1),
    path('2',tela2),
    path('3',ficha_cadastro,name='ficha_cadastro'),
    path('4',chave,name='chave_estrangeira'),
    path('5',listar_chave,name='listar_chaves'),
    path('6',manytomany,name="muitos"),
    path('listar/<int:id>/',listar_dinamico,name='listar_dinamico')
]