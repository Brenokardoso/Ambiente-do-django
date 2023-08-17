from django.contrib import admin
from django.urls import path,include
from .views import tela1,tela2,ficha_cadastro,chave


urlpatterns = [
    path('1/',tela1),
    path('2',tela2),
    path('3',ficha_cadastro,name='ficha_cadastro'),
    path('4',chave,name='chave_estrangeira')
]