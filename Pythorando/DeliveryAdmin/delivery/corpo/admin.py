from django.contrib import admin
from .models import Pessoa,Cargo,Pedido
from django_object_actions import DjangoObjectActions
from django.http import HttpResponse




class PedidoInLine(admin.TabularInline):
    list_display = ('nome','quantidade','descricao')
    model = Pedido
    extra = 0


@admin.register(Pessoa)
class PessoaAdmin(DjangoObjectActions,admin.ModelAdmin):
    inlines = [PedidoInLine]
    list_display = ('get_pega_foto','nome','email','senha','cargo','nome_sobrenome')
    list_editable = ('nome',)
    readonly_fields = ('senha','cargo')
    list_filter = ('nome',)
    search_fields = ('email',)

    def mostra_pessoa(self,request,pessoa_referencia):
        return HttpResponse(pessoa_referencia)
    
    mostra_pessoa.label = "mostra_pessoa" # Esse campo que mostra oq estaŕa escrito no botão
    change_actions = ("mostra_pessoa",) #registra  o botão




admin.site.register(Cargo)
