from django.urls import path, include
from rest_framework import routers
from api.viewsets import DonorsViewSet

router = routers.DefaultRouter()
router.register(r'donors', DonorsViewSet)

urlpatterns = [
    path('', include(router.urls))
]
