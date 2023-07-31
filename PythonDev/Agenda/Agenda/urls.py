
from django.contrib import admin
from django.urls import path
from core.views import lista_eventos,teste,index
from core.models import Evento


urlpatterns = [
    path('admin/', admin.site.urls),    
    path('',index),
    path('agenda/',lista_eventos),
    path('teste/',teste)
]
