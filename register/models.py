from django.db import models

# Create your models here.
class Registration(models.Model):
    team_name = models.TextField()
    team_members = models.IntegerField()
    manager = models.TextField()
    coach = models.TextField()
class Admin(models.Model):
    username = models.TextField()
    password = models.TextField()
class Score(models.Model):
    score = models.TextField()
    team = models.TextField()