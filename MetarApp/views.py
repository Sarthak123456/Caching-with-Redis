from django.shortcuts import render
from django.db import models
from django.conf import settings
from django.shortcuts import render, redirect
from .models import metar
# Create your views here.

def view(request):
        post= metar.objects.all()[:200]

        context={'posts' : post}    
        return render(request, 'view.html', context)
   
    
def final(request, scode):
        post_data=metar.objects.get(scode=scode)
        context={"post_data": post_data}
        return render(request, 'final.html', context)
