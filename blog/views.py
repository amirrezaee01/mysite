from django.shortcuts import render,get_object_or_404
from blog.models import Post
import datetime

def blog_view(request):
    now = datetime.datetime.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request, pid):
    # Get all published posts ordered by ID
    posts = Post.objects.filter(status=1).order_by('id')
    
    # Get the current post
    post = get_object_or_404(posts, id=pid)
    
    # Update view count
    post.counted_views += 1
    post.save()
    
    # Find the index of the current post
    post_ids = [post.id for post in posts]
    current_index = post_ids.index(post.id)
    
    # Determine previous and next posts
    prev_post = None
    next_post = None
    
    if current_index > 0:
        prev_post_id = post_ids[current_index - 1]
        prev_post = get_object_or_404(Post, id=prev_post_id, status=1)
    
    if current_index < len(post_ids) - 1:
        next_post_id = post_ids[current_index + 1]
        next_post = get_object_or_404(Post, id=next_post_id, status=1)
    
    # Prepare context
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    
    return render(request, 'blog/blog-single.html', context)

def test(request,pid):
    post = get_object_or_404(Post,id=pid)
    context = {'post':post}
    return render(request,'test.html',context)