from django.shortcuts import render,get_object_or_404
from blog.models import Post
import datetime

def blog_view(request):
    now = datetime.datetime.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request,pid):
    posts = Post.objects.filter(status=1)
    post = get_object_or_404(posts,id=pid)
    post.counted_views+= 1
    post.save()
    context = {'post':post}
    return render(request, 'blog/blog-single.html',context)

def test(request,pid):
    post = get_object_or_404(Post,id=pid)
    context = {'post':post}
    return render(request,'test.html',context)