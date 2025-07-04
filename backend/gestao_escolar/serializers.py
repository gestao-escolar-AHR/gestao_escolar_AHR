from rest_framework.serializers import ModelSerializer

from .models import Curso, Aluno, Disciplina, Professor, Nota, Matricula, Turma

class TurmaSerializer(ModelSerializer):
    class Meta:
        model = Turma
        fields = '__all__'

class CursoSerializer(ModelSerializer):
    class Meta:
        model = Curso
        fields = '__all__'

class AlunoSerializer(ModelSerializer):
    class Meta:
        model = Aluno
        fields = '__all__'

class DisciplinaSerializer(ModelSerializer):
    class Meta:
        model = Disciplina
        fields = '__all__'

class ProfessorSerializer(ModelSerializer):
    class Meta:
        model = Professor
        fields = '__all__'

class NotaSerializer(ModelSerializer):
    class Meta:
        models = Nota
        fields = '__all__'

class MatriculaSerializer(ModelSerializer):
    class Meta:
        models = Matricula
        fiels = '__all__'