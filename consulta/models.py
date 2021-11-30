from django.db import models


class consulta(models.Model):
    especialidade = models.CharField(max_length=30)
    mostrar = models.BooleanField(default=True)
    data = models.DateField()
    horario = models.TimeField()
    nome_paciente = models.CharField(max_length=50, blank=True, null=True)
    nome_medico = models.CharField(max_length=50)


