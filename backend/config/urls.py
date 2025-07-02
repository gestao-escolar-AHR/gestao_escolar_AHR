from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter
from gestao_escolar.views import AlunoViewSet

router = DefaultRouter()
router.register(r'alunos', AlunoViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
]
