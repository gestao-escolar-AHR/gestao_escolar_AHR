from django.db import models

class Aluno(models.Model):
    nome = models.CharField(max_length=45)
    CPF = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=45)
    pai = models.CharField(max_length=45)
    mae = models.CharField(max_length=45)
    data_nasc = models.DateField

    def __str__(self):
        return f'{self.nome} ({self.email})'