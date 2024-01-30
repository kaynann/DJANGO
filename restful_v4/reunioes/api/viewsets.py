from rest_framework import viewsets
from .serializers import MeetingSerializer
from reunioes.models import Meeting

class MeetingViewSet(viewsets.ModelViewSet):
  queryset = Meeting.objects.all()
  serializer_class = MeetingSerializer