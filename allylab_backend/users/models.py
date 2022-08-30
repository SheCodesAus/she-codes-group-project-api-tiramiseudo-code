from django.db import models

# Create your models here.
class Project(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=50)
  email = models.EmailField(max_length=50)
  password = models.CharField(max_length=50)
  pronoun = models.CharField(max_length=10)
  photo = models.CharField(max_length=200)
  bio = models.CharField(max_length=1000)