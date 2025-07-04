from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from gestao_escolar.views import CursoViewSet, AlunoViewSet, DisciplinaViewSet, ProfessorViewSet, NotaViewSet, MatriculaViewSet, TurmaViewSet

router = DefaultRouter()

router.register(r'cursos', CursoViewSet)
router.register(r'alunos', AlunoViewSet)
router.register(r'disciplinas', DisciplinaViewSet)
router.register(r'professores', ProfessorViewSet)
router.register(r'notas', NotaViewSet)
router.register(r'matriculas', MatriculaViewSet)
router.register(r'turmas', TurmaViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
