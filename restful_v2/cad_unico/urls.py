from django.urls import path, include
from rest_framework import routers
from .api.viewsets import BeneficiaresViewSet

router = routers.DefaultRouter()
router.register(r'beneficiares', BeneficiaresViewSet)

urlpatterns = [
    path('', include(router.urls))
]
