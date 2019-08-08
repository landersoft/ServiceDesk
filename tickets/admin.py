from django.contrib import admin
from .models import Ticket

# Register your models here.



class AdminTicket(admin.ModelAdmin):
    list_display = ["fecha", "ccmm","ticket","analista","resumen","asignatario", "estado","grupo_resolutor","fecha_derivacion","solucionable_cau"]
    list_filter = ["asignatario","ccmm"]
    search_fields = ["ticket"]

    class Meta:
        model = Ticket



admin.site.register(Ticket, AdminTicket)