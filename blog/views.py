from django.shortcuts import render, redirect

from . models import Blog
from . forms import BlogForm

def opiniones(request):
    if request.method == "POST":
        form = BlogForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('opiniones')
        else:
            form = BlogForm()

    publicaciones = Blog.objects.all()

    return render(request, 'blog/blog.html', {'form': form, 'opiniones': publicaciones})
        

def blog(request):
    publicaciones = Blog.objects.all()
    return render(request,"blog/blog.html", {"publicaciones":publicaciones})


# Create your views here.
