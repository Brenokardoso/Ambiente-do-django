from django.urls import path,include
from .views import cadastro,home,tela1

urlpatterns = [
    path('cadastro/',cadastro),
    path('',home),
    path('tela/',tela1,name="tela_url")
]