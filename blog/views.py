from django.shortcuts import render, get_object_or_404
from .models import Post
# Create your views here.

def bloghome(request):
    allPosts=Post.objects.all()
    context={'allPosts':allPosts}
    return render(request, 'blog/bloghome.html',context)
def blogpost(request, slug):
    post = get_object_or_404(Post, slug=slug)
    context = {'post': post}
    return render(request, 'blog/blogpost.html', context)

