from django.db import models

# Create your models here.

PRONOUNS = [
  ('S', 'She/her/hers'),
  ('H', 'He/him/his'),
  ('T', 'They/them/theirs'),
  ('O', 'Other'),
]

from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
  username = None
  email = models.EmailField(unique=True)
  first_name = models.CharField(max_length=30)
  last_name = models.CharField(max_length=50)
  password = models.CharField(max_length=50)
  pronoun = models.CharField(max_length=10, choices=PRONOUNS)
  photo = models.URLField()
  bio = models.CharField(max_length=1000)
  skills = models.ManyToManyField('Skill', related_name="users")

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS =[]
  
  def __str__(self):
    return self.email
class Skill(models.Model):
  skill_name = models.CharField(max_length=30)
  icon = models.URLField()
  # date_created = models.DateTimeField()


