from django.urls import path
from .views import listar_tarefas, cadastrar_tarefa, excluir_tarefa

# Adicione as demais URLs conforme necessário
urlpatterns = [
    path('', listar_tarefas, name='listar_tarefas'),
    path('listar/', listar_tarefas, name='listar_tarefas'),
    path('cadastrar/', cadastrar_tarefa, name='cadastrar_tarefa'),
    path('excluir/<int:tarefa_id>/', excluir_tarefa, name='excluir_tarefa'),
    
]