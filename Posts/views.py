from django.shortcuts import render, redirect, get_object_or_404
from .models import Post

def post(request):
    if request.method == "POST":
        title = request.POST.get("title")
        image = request.FILES.get("image")
        if title:
            Post.objects.create(title=title, image=image)
        return redirect('post') 

    posts = Post.objects.all().order_by('-id')
    return render(request, 'post.html', {'posts': posts})

def delete_post(request, post_id):
    post = get_object_or_404(Post, id=post_id)
    post.delete()
    return redirect('post')
