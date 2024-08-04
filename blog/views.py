from django.shortcuts import render,get_object_or_404
from blog.models import Post
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage

def blog_view(request, **kwargs):
    now = timezone.now()
    posts = Post.objects.filter(published_date__lte=now, status=1)
    
    if kwargs.get('cat_name'):
        posts = posts.filter(category__name=kwargs['cat_name'])
    if kwargs.get('author_firstname'):
        posts = posts.filter(author__first_name=kwargs['author_firstname'])
    if kwargs.get('tag_name'):
        posts = posts.filter(tags__name__in=[kwargs['tag_name']])
        
        
    posts = Paginator(posts,3)
    try:
        page_number = request.GET.get('page')
        posts = posts.get_page(page_number)
    except PageNotAnInteger:
        posts = posts.get_page(1)
    except EmptyPage:
        posts = posts.get_page(1)
        
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)


def blog_single(request, pid):
    now = timezone.now()
    
    # Fetch the specific post
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=now)
    
    # Increment the view count
    post.counted_views += 1
    post.save()
    
    # Fetch the ordered posts
    posts = Post.objects.filter(status=1, published_date__lte=now).order_by('published_date')
    
    # Get the list of post IDs
    post_ids = list(posts.values_list('id', flat=True))
    current_index = post_ids.index(post.id)
    
    # Determine the previous and next post
    prev_post = posts[current_index - 1] if current_index > 0 else None
    next_post = posts[current_index + 1] if current_index < len(post_ids) - 1 else None
    
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
    }
    
    return render(request, 'blog/blog-single.html', context)

def test(request):
    return render(request,'test.html',)

def blog_search(request):
    posts = Post.objects.filter(status=1)
    if request.method == 'GET':
        if s:= request.GET.get('s'):
            posts = posts.filter(content__contains=s)
    context = {'posts':posts}
    return render(request, 'blog/blog-home.html',context)
    



    