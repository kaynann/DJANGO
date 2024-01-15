from django.db import models

class Livro(models.Model):
  book_name = models.CharField(max_length=100)
  year_of_publication = models.IntegerField()
  number_pages = models.IntegerField()
  author_name = models.CharField(max_length=100)
  publishing_company = models.CharField(max_length=100)
  price = models.FloatField(default=0.0)

  def __str__(self):
    return self.book_name