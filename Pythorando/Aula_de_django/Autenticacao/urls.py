from django.urls import path,include
from . import views
from .views import cadastro,home

urlpatterns = [
    path('cadastro/',cadastro),
    path('',home),
]