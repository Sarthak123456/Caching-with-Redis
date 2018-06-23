from django.db import models
from django.conf import settings
import os
# Create your models here.
class metar(models.Model):
   # user = models.ForeignKey(User, unique=True)
    scode=models.CharField(max_length=15)
    scode_text=models.CharField(max_length=1000)
    
    def __str__(self):
        return self.scode