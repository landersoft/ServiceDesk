from django.contrib import admin
from .models import Ticket, CCMM, Analista, Grupo, Asignatario


# Register your models here.



class AdminTicket(admin.ModelAdmin):
    list_display = ["ticket","fecha", "ccmm","analista","resumen","asignatario", "estado","grupo_resolutor","fecha_derivacion","solucionable_cau"]
    list_filter = ["fecha","asignatario"]
    search_fields = ["ticket"]
    autocomplete_fields = ['ccmm']

    class Meta:
        model = Ticket

class AdminCCMM(admin.ModelAdmin):
    list_display=["sigla"]
    list_filter = ["sigla"]
    search_fields = ["sigla"]

    class Meta:
        model = CCMM


admin.site.register(Ticket, AdminTicket)
admin.site.register(CCMM, AdminCCMM)
admin.site.register(Grupo)
admin.site.register(Analista)
admin.site.register(Asignatario)