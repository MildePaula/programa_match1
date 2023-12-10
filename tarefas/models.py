
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

class Tarefa(models.Model):
    descricao = models.CharField(max_length=255)
    data_vencimento = models.DateField()
    prioridade = models.IntegerField(
        validators=[
            MinValueValidator(1, message="A prioridade deve ser no mínimo 1."),
            MaxValueValidator(5, message="A prioridade deve ser no máximo 5."),
        ]
    )

    def __str__(self):
        return self.descricao