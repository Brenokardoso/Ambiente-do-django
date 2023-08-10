from django.urls import path,include
from django.http import HttpResponse
from .views import *

urlpatterns = [
    path('tela1/',tela1),
    path('formulario/', form , name = 'formulario'),
    path('mostrar/', view_form_data),
]