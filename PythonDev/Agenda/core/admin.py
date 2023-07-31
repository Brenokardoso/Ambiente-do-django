from django.contrib import admin
from core.models import Evento


class EventoAdmin(admin.ModelAdmin):
    list_display = ("titulo","numero","descricao","usuario")
    list_filter = ("titulo",)


admin.site.register(Evento,EventoAdmin)
