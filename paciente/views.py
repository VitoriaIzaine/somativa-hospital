from django.shortcuts import render, get_object_or_404


def index_paciente(request):
    return render(request, 'paciente/index_paciente.html')

def agendamento(request):
    return render(request, 'paciente/agendamento_consulta.html')




