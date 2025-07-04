from django.db import models
    
class Curso(models.Model):
    nome = models.CharField(max_length=45)
    carga_horaria = models.IntegerField(default=0)
    descricao = models.CharField(max_length=100)

    def __str__(self):
        return f'{self.nome} - {self.carga_horaria}h'

class Aluno(models.Model):
    nome = models.CharField(max_length=45)
    CPF = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField(max_length=45)
    pai = models.CharField(max_length=45)
    mae = models.CharField(max_length=45)
    data_nasc = models.DateField(null=True)

    def __str__(self):
        return f'{self.nome} ({self.email})'

class Professor (models.Model): 
    nome = models.CharField(max_length=45)
    CPF = models.CharField(max_length=11)
    telefone = models.CharField(max_length=11)
    email = models.EmailField (max_length=45)
    data_nasc = models.DateField(null=True)
    formacao = models.CharField(max_length=45)
    
    def __str__(self):
        return f'{self.nome} - {self.email}'
    
    class Meta:
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'
    
class Turma(models.Model):
    quantidade_alunos = models.IntegerField(default=0)
    sala_turma = models.CharField(max_length=45)
    nome_turma = models.CharField(max_length=45)

    def __str__(self):
        return f'{self.nome_turma} - {self.sala_turma}'

class Disciplina (models.Model):
    nome = models.CharField(max_length=45)
    descricao = models.CharField(max_length=45)
    carga_horaria = models.IntegerField()
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    professor = models.ForeignKey(Professor, on_delete=models.PROTECT)
    
    def __str__(self):
         return f'{self.nome} - {self.carga_horaria}h'
    
class Nota (models.Model):
    nota = models.DecimalField(max_digits=4, decimal_places=2)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)
 
    def __str__(self):
         return f'{self.nota} - {self.disciplina.nome}'
    
class Matricula (models.Model):
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    curso = models.ForeignKey(Curso, on_delete=models.PROTECT)
    data_matricula = models.DateField(null=True)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return f'{self.aluno.nome} - {self.data_matricula}'
    
    class Meta: 
        verbose_name = 'Matrícula'
    
class Aula (models.Model):
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, null=True)
    disciplina = models.ForeignKey(Disciplina, on_delete=models.PROTECT)

    def __str__(self):
        return f'{self.turma.sala_turma} - {self.disciplina.nome}'
    
class Frequencia (models.Model):
    data = models.DateField(null=True)
    aluno = models.ForeignKey(Aluno, on_delete=models.PROTECT)
    turma = models.ForeignKey(Turma, on_delete=models.PROTECT, null=True)
    
    class Meta: 
        verbose_name = 'Frequência'
    
    

