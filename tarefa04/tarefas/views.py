from django.shortcuts import render
from .models import Tarefa
from datetime import date

def lista_tarefas(request):
    tarefas = Tarefa.objects.all()
    hoje = date.today()
    return render(request, 'tarefas/index.html', {'tarefas': tarefas, 'hoje': hoje})