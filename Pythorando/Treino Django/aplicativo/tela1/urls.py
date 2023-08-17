from django.contrib import admin
from django.urls import path,include
from .views import tela1,tela2,ficha_cadastro


urlpatterns = [
    path('1/',tela1),
    path('2',tela2),
    path('3',ficha_cadastro)
]