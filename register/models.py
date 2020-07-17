from django.db import models

# Create your models here.
class Registration(models.Model):
    team_name = models.TextField()
    team_members = models.IntegerField()
    manager = models.TextField()
    coach = models.TextField()
    