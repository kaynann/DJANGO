from django.db import models

class Donors(models.Model):
  name = models.CharField(max_length=60)
  surname = models.CharField(max_length=60)
  blood_type = models.CharField(max_length=3)
  donor = models.BooleanField(default=False)

  def __str__(self):
    return self.name