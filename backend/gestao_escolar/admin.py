from django.contrib import admin
from  .models import Curso, Aluno, Professor, Disciplina

admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
