from consulta import views
from django.urls import path


urlpatterns = [
    path("", views.agendamento, name='agendamento'),
    path('salvar/<int:idbus>', views.salvar, name='salvar'),
    path('paciente/<int:idbus>', views.mostrar_paciente, name='mostrar_paciente'),

]
