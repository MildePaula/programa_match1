from django.shortcuts import render, redirect, get_object_or_404
from .models import Tarefa
from .forms import TarefaForm

def cadastrar_tarefa(request):
    if request.method == 'POST':
        form = TarefaForm(request.POST)
        if form.is_valid():
            form.save()
            # Adiciona uma mensagem de sucesso para ser exibida na próxima página
            request.session['mensagem_sucesso'] = 'Tarefa cadastrada com sucesso!'
            return redirect('listar_tarefas')
        else:
            # Adiciona uma mensagem de erro para ser exibida na página atual
            request.session['mensagem_erro'] = 'Erro ao cadastrar a tarefa. Por favor, corrija os campos abaixo.'
            return render(request, 'tarefas/cadastrar_tarefa.html', {'form': form})
    else:
        form = TarefaForm()

    # Limpa a mensagem de erro da sessão, caso exista
    request.session.pop('mensagem_erro', None)

    return render(request, 'tarefas/cadastrar_tarefa.html', {'form': form})

def listar_tarefas(request):
    tarefas = Tarefa.objects.order_by('prioridade')
    return render(request, 'tarefas/listar_tarefas.html', {'tarefas': tarefas})


def excluir_tarefa(request, tarefa_id):
    tarefa = get_object_or_404(Tarefa, id=tarefa_id)
    tarefa.delete()
    request.session['mensagem_sucesso'] = 'Tarefa excluída com sucesso!'
    return redirect('listar_tarefas')