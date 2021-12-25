from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Article(models.Model):
    name = models.CharField(max_length=100)
    description =models.CharField(max_length=250)
    email = models.EmailField(max_length=100)
    createdAt = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return self.name

    
