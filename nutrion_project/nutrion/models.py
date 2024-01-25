from django.db import models
from django.contrib.auth.models import User

class Food(models.Model):
  name = models.CharField(max_length=100)
  carbohydrate = models.FloatField()
  proteins = models.FloatField()
  fats = models.FloatField()
  calories = models.FloatField()

  def __str__(self):
    return self.name

class Consumed(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  consumed_food = models.ForeignKey(Food, on_delete=models.CASCADE)