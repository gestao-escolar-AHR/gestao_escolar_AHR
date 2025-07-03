from rest_framework.serializers import ModelSerializer

from .models import Curso, Aluno, Disciplina, Professor

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