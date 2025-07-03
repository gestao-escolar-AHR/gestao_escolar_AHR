from django.contrib import admin

from  .models import Curso, Aluno, Professor, Disciplina, Nota

admin.site.register(Curso)
admin.site.register(Aluno)
admin.site.register(Professor)
admin.site.register(Disciplina)
admin.site.register(Nota)
