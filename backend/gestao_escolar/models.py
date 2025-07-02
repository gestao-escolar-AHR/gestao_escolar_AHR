from django.db import models

class Curso(models.Model):
    nome = models.CharField(max_length=45)
    carga_horaria = models.IntegerField(default=0)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome}'