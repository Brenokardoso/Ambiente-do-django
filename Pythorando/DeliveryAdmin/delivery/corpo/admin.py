from django.contrib import admin
from .models import Pessoa,Cargo,Pedido


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    list_display = ('nome','email','senha','cargo')
    readonly_fields = ('senha',)
    list_filter = ('nome',)
    search_fields = ('email',)

admin.site.register(Cargo)
admin.site.register(Pedido)