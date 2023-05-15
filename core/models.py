from django.db import models

# Create your models here.

class Keywords(models.Model):
    
    word= models.CharField(null=False, blank=False, min_length=3, max_length=50)
