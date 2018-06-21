from django.shortcuts import render
from django.db import models
from django.conf import settings
from django.shortcuts import render, redirect
from .models import metar
# Create your views here.

def view(request):
        post= metar.objects.all()[:20]

        context={'posts' : post}    
        return render(request, 'view.html', context)
   