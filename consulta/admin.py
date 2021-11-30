from django.contrib import admin
from .models import consulta


@admin.register(consulta)
class detConsulta(admin.ModelAdmin):
    list_display = ('id', 'nome_medico', 'especialidade', 'data', 'mostrar','horario','nome_paciente')