from django.shortcuts import render
from . models import About, Skills

def about(request):
    formacion = About.objects.all()
    skills = Skills.objects.all()
    return render(request, "about/about.html", {"formacion": formacion, "skills": skills})

# Create your views here.
