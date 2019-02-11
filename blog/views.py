from django.shortcuts import render, get_object_or_404
from .models import Post

# Create your views here.

class PostView:
    def index(request):
        posts = Post.objects.all()

        return render(request, 'index.html', { 'posts': posts })
    
    def detail(request, id):
        post = get_object_or_404(Post, pk=id)

        return render(request, 'detail.html', { 'post': post })
        
        