from django import forms
from .models import Tarefa

class TarefaForm(forms.ModelForm):
    class Meta:
        model = Tarefa
        fields = ['descricao', 'data_vencimento', 'prioridade']

    def clean_prioridade(self):
        prioridade = self.cleaned_data['prioridade']

        # Defina o intervalo de prioridade desejado
        valor_minimo = 1
        valor_maximo = 5

        if not valor_minimo <= prioridade <= valor_maximo:
            raise forms.ValidationError(f"A prioridade deve estar entre {valor_minimo} e {valor_maximo}.")

        return prioridade