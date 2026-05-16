from django.shortcuts import render,redirect
from .models import Blog
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def addBlogView(request):
    if request.method=="POST":
        title=request.POST.get("title")
        description=request.POST.get("description")
        blog_image=request.FILES["blog_image"]
        blog=Blog()
        blog.title=title
        blog.description=description
        blog.blog_image=blog_image
        blog.user=request.user
        blog.save()

        return redirect("/home")

    else:
     return render(request,"blogform.html")