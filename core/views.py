from django.shortcuts import render, HttpResponse

def home(request):
    return render(request, template_name="core/home.html")

def contacto(request):
    return render(request, "core/contacto.html")