from django.shortcuts import render

from .models import Blog
    

def blog(request):
    publicaciones = Blog.objects.all()
    return render(request,"blog/blog.html", {"publicaciones":publicaciones})
