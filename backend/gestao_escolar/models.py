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

class Professor (models.Model): 
    nome = models.CharField(max_length=45)
    CPF = models.IntegerField(default=0)
    telefone = models.IntegerField(default=0)
    email = models.EmailField (max_length=45)
    data_nasc = models.DateField(null=True)
    formacao = models.CharField(max_length=45)
    
    def _str_(self):
        return f'{self.nome} - {self.email}'

class Disciplina (models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    
    def _str_(self):
         return f'{self.nome} - {self.carga_horaria}'
