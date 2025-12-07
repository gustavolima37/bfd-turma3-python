from django.contrib import admin
from .models import Consulta

# Register your models here.

@admin.register(Consulta)
class ConsultaAdmin(admin.ModelAdmin):
    list_display = ("paciente", "medico", "data", "status")
    list_filter = ("status", "medico")
    search_fields = ("paciente_nome", "medico_nome")