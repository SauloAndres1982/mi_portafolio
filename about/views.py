from django.shortcuts import render
from . models import About

def about(request):
    formacion = About.objects.all()
    return render(request, "about/about.html", {"formacion": formacion})

# Create your views here.
