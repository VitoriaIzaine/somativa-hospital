from django.urls import path
from . import views

urlpatterns = [
    path("", views.index_paciente, name='index_paciente'),
    path("agendamento", views.agendamento, name='agendamento'),
]