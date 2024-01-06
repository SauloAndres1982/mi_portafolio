from django.shortcuts import render

from . models import Post, Comment
from .forms import CommentForm


def index(request):
    post = Post.objects.all()
    return render(request, "post/index.html", {"post":post})

def post_detail(request, post_id):
    post = Post.objects.get(id=post_id)
    
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            new_form = form.save(commit=False) 
            new_form.post = post
            new_form.save()
            
    else:
        form = CommentForm() 
    
    comments  = post.comments.filter(active=True)
    return render(request, "post/post_detail.html", {"post":post, "comments": comments, "form": form})