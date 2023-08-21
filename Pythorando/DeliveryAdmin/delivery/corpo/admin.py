from django.contrib import admin
from .models import Pessoa,Cargo,Pedido




class PedidoInLine(admin.TabularInline):
    list_display = ('nome','quantidade','descricao')
    model = Pedido
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [PedidoInLine]
    list_display = ('foto','nome','email','senha','cargo','nome_sobrenome')
    # readonly_fields = ('senha','cargo')
    list_filter = ('nome',)
    search_fields = ('email',)


# @admin.register(Pedido)
# class PedidoAdmin(admin.ModelAdmin):
#     list_display = ('nome','quantidade','descricao')
#     readonly_fields = ('pessoa',)


admin.site.register(Cargo)
