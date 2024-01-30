from rest_framework import serializers
from reunioes.models import Meeting

class MeetingSerializer(serializers.ModelSerializer):
  class Meta:
    model = Meeting
    fields = '__all__'