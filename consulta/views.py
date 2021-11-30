from django.shortcuts import render, get_object_or_404
from .models import consulta


def agendamento(request):
    info = consulta.objects.all()
    return render(request, 'consulta/agendamento_consulta.html', {'info': info})

def mostrar_paciente(request, idbus):
    info = get_object_or_404(consulta, id=idbus)
    return render(request, 'consulta/detconsulta.html', {'info': info})


def salvar(request, idbus):
    tudo = consulta.objects.get(id=idbus)
    print(tudo.nome_paciente)
    print(request.POST.get('nome'))

    tudo.nome_paciente = request.POST.get('nome')
    tudo.save()

    return render(request, 'home/index.html')



