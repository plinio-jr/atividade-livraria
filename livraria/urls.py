from django.contrib import admin
from core.views import CategoriaViewSet, EditoraViewSet
from django.urls import include, path

from rest_framework.routers import DefaultRouter

from core.views import CategoriaViewSet

router = DefaultRouter()
router.register(r'categorias', CategoriaViewSet)
router.register(r'categorias', CategoriaViewSet)
router.register(r'editoras', EditoraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
]