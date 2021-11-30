from django.contrib import admin
from .models import cadastro_medicos


@admin.register(cadastro_medicos)
class detMedico(admin.ModelAdmin):
    list_display = ('id', 'nome', 'especialidade', 'foto', 'mostrar')