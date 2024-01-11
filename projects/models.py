from django.db import models

# Create your models here.

# modulo projects
class Project(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    technology = models.CharField(max_length=200)
    create_date = models.DateTimeField(auto_now_add=True)
