from django.db import models

class Professor (models.Model): 
    nome = models.CharField(max_length=45)
    CPF = models.IntegerField(default=0)
    telefone = models.IntegerField(default=0)
    email = models.EmailField (max_length=45)
    data_nasc = models.DateField(null=True)
    formacao = models.CharField(max_length=45)
    
    def _str_(self):
        return f'{self.nome} - {self.email}'