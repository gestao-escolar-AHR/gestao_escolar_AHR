from django.db import models

class Disciplina (models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    
    def _str_(self):
         return f'{self.nome} - {self.carga_horaria}'
