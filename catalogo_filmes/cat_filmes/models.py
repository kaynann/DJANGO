from django.db import models

class Movie(models.Model):
  GENDER_CHOICES = (
    ('AC', 'Ação'),
    ('AV', 'Aventura'),
    ('RO', 'Romance'),
    ('TE', 'Terror'),
    ('DR', 'Drama'),
    ('SU', 'Suspense'),
    ('FC', 'Ficção Cientifíca'),
    ('CO', 'Comédia'),
    ('DO', 'Documentário'),
    ('AN', 'Animação'),
    ('NI', 'Não informado')
  )

  name = models.CharField(max_length=120)
  director = models.CharField(max_length=60)
  synopsis = models.TextField()
  release_year = models.DateField() 
  duration = models.IntegerField(default=0)
  gender = models.CharField(max_length=2, choices=GENDER_CHOICES, default='NI')
  date_register = models.DateTimeField(auto_now_add=True)
  photo = models.ImageField(upload_to='capas', null=True, blank=True)

  def __str__(self):
    return self.name