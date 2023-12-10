# Generated by Django 5.0 on 2023-12-10 20:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tarefas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tarefa',
            name='prioridade',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1, message='A prioridade deve ser no mínimo 1.'), django.core.validators.MaxValueValidator(5, message='A prioridade deve ser no máximo 5.')]),
        ),
    ]
