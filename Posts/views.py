from django.shortcuts import render, redirect
from .models import Post

def post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        if title:
            Post.objects.create(title=title, image=image)
        return redirect('post') 

    posts = Post.objects.all()
    return render(request, 'post.html', {'posts': posts})
