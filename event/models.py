from django.db import models

# Create your models here.
class hackathon(models.Model):
    title = models.CharField(max_length=20)
    desc = models.TextField(max_length = 150)
    date = models.DateTimeField()
    venue = models.CharField(max_length = 20)