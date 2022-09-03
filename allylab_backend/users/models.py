from django.db import models

# Create your models here.

PRONOUNS = [
  ('S', 'She/her/hers'),
  ('H', 'He/him/his'),
  ('T', 'They/them/theirs'),
  ('O', 'Other'),
]
class User(models.Model):
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=50)
  email = models.EmailField()
  password = models.CharField(max_length=50)
  pronoun = models.CharField(max_length=10, choices=PRONOUNS)
  photo = models.URLField()
  bio = models.CharField(max_length=1000)
  skills = models.ManyToManyField('Skill', related_name="users")

class Skill(models.Model):
  skill_name = models.CharField(max_length=30)
  icon = models.URLField()
