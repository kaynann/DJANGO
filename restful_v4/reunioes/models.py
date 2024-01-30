from django.db import models

class Meeting(models.Model):
  title = models.CharField(max_length=120)
  description = models.TextField()
  local = models.TextField()
  participant_name = models.CharField(max_length=60)
  date_time = models.DateTimeField()

  def __str__(self):
    return self.participant_name