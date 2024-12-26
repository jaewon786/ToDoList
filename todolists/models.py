from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Todo(models.Model):
  author = models.ForeignKey(User, on_delete=models.CASCADE)
  content = models.TextField()
  create_date = models.DateTimeField()
  
  def __str__(self):
    return self.content