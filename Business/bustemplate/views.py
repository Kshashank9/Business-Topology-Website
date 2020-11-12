from django.shortcuts import render
from .models import courses

# Create your views here.
def index(request): 
    course=courses.objects.all()

    return render(request,"index.html",{'course':course})

