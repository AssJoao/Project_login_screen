from django.db import models

# Createe your models here.
class TarefaModel(models.model):
    nome = models.charfield(max_length=100)
    descricao = models.TextField(null=True,blank=True)
    completo = models.BooleanField(default=False)
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome