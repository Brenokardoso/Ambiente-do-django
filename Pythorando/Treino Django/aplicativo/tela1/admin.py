from django.contrib import admin
from tela1.models import Pessoa,Cargo,Data,Pedidos


admin.site.register(Cargo)


class PedidosInLine(admin.TabularInline):
    model = Pedidos
    list_display = ("nome","quantidade","tempo_de_espera","total_a_pagar")
    extra = 0

@admin.register(Pessoa)
class PessoaAdmin(admin.ModelAdmin):
    inlines = [PedidosInLine]
    list_display = ('nome', 'email', 'senha', 'cargo')
    # readonly_fields = ('senha',)
    search_fields = ('nome', 'cargo__nome')  # Pesquisar pelo nome do cargo
    # list_display_links = ('senha',)

@admin.register(Data)
class DataAdmin(admin.ModelAdmin):
    list_display = ('data',)

# @admin.register(Pedidos)
# class PedidosAdmin(admin.ModelAdmin):
#     list_display = ("nome","quantidade","tempo_de_espera","total_a_pagar")
#     list_editable = ("tempo_de_espera",)

