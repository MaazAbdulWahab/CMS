from django.db import models

# Create your models here.


class Keywords(models.Model):
    word = models.CharField(null=False, blank=False, max_length=50)
