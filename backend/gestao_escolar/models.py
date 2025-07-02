from django.db import models
    
class Nota (models.Model):
    nota = models.DecimalField((""), max_digits=4, decimal_places=2)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
 
    def __str__(self):
         return f'{self.disciplina} - {self.nota}'