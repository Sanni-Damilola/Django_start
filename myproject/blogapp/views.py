from django.shortcuts import render
from .models import BlogPost

# Create your views here.
def archive(req):
    blogs = BlogPost.objects.all()
    data = {
        "blogs": blogs
    }
    return render(req, "blog/archive.html", data)

def details(req, pk):
    blogs = BlogPost.objects.get(pk=pk)
    return render(req, "blog/details.html", {"blogs": blogs})
