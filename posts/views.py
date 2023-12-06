from django.shortcuts import render
from .models import Post

# Create your views here.


def index(req):
    posts=Post.objects.all()
    return render(req,'index.html',{'posts':posts})

def post(req,pk):
    posts=Post.objects.get(id=pk)
    return render(req,'post.html',{'posts':posts})