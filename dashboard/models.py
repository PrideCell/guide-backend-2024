from django.db import models

# Create your models here.

class Log(models.Model):
    timestamp = models.DateTimeField(auto_now_add=True)
    team_id = models.CharField(max_length=200)
    action = models.TextField()
