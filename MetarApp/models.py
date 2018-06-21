from django.db import models
from django.conf import settings
import os
# Create your models here.
class metar(models.Model):
   # user = models.ForeignKey(User, unique=True)
    scode=models.TextField(max_length=1000)
    
    def __str__(self):
        return self.scode