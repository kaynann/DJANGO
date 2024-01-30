from django.urls import path, include
from .views import index, register, delete_meeting
from rest_framework import routers
from .api.viewsets import MeetingViewSet

router = routers.DefaultRouter()
router.register(r'api_reunioes', MeetingViewSet)

urlpatterns = [
    path('', index, name='index'),
    path('register', register, name='register'),
    path('delete/<int:id>', delete_meeting, name='delete'),
    path('api_reunioes', include(router.urls)),
]
