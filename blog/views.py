from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone

def blog_view(request):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)

def blog_single(request, pid):
    now = timezone.now()
    
    posts = Post.objects.filter(status=1, published_date__lte=now).order_by('id')
    
    post = get_object_or_404(posts, id=pid)
    
    post.counted_views += 1
    post.save()
    
    post_ids = [post.id for post in posts]
    current_index = post_ids.index(post.id)
    
    prev_post = None
    next_post = None
    
    if current_index > 0:
        prev_post_id = post_ids[current_index - 1]
        prev_post = get_object_or_404(Post, id=prev_post_id, status=1, published_date__lte=now)
    
    if current_index < len(post_ids) - 1:
        next_post_id = post_ids[current_index + 1]
        next_post = get_object_or_404(Post, id=next_post_id, status=1, published_date__lte=now)
    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    
    return render(request, 'blog/blog-single.html', context)


def test(request):
    return render(request,'test.html',)

def blog_category(request,cat_name):
    posts = Post.objects.filter(status=1)
    posts = posts.filter(category__name=cat_name)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)
