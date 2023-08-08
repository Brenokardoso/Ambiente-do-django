from django.contrib import admin
from django.urls import path,include




urlpatterns = [
    path('admin/', admin.site.urls),
    path('autenticacao/',include("Autenticacao.urls")),
    path('telas/',include("telas.urls")),
]
