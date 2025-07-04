from rest_framework.viewsets import ModelViewSet

from .models import Curso, Aluno, Disciplina, Professor, Nota, Matricula, Turma, Aula, Frequencia
from .serializers import CursoSerializer, AlunoSerializer, DisciplinaSerializer, ProfessorSerializer, NotaSerializer, MatriculaSerializer, TurmaSerializer, AulaSerializer, FrequenciaSerializer

class CursoViewSet(ModelViewSet):
    queryset = Curso.objects.all()
    serializer_class = CursoSerializer

class AlunoViewSet(ModelViewSet):
    queryset = Aluno.objects.all()
    serializer_class = AlunoSerializer

class DisciplinaViewSet(ModelViewSet):
    queryset = Disciplina.objects.all()
    serializer_class = DisciplinaSerializer

class ProfessorViewSet(ModelViewSet):
    queryset = Professor.objects.all()
    serializer_class = ProfessorSerializer
    
class NotaViewSet(ModelViewSet):
    queryset = Nota.objects.all()
    serializer_class = NotaSerializer

class MatriculaViewSet(ModelViewSet):
    queryset = Matricula.objects.all()
    serializer_class = MatriculaSerializer

class TurmaViewSet(ModelViewSet):
    queryset = Turma.objects.all()
    serializer_class = TurmaSerializer

class AulaViewSet(ModelViewSet):
    queryset = Aula.objects.all()
    serializer_class = AulaSerializer
    
class FrequenciaViewSet(ModelViewSet):
    queryset = Frequencia.objects.all()
    serializer_class = FrequenciaSerializer