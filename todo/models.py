from django.db import models

# Create your models here.
class todolist(models.Model):
    listid = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
