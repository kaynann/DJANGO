from django.urls import path, include
from .views import index, register
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers
from .api.viewsets import MovieViewSet

router = routers.DefaultRouter()
router.register(r'api_filmes', MovieViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('api_filmes', include(router.urls)),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
