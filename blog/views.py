from django.shortcuts import render,get_object_or_404
from blog.models import Post,Comment
from django.utils import timezone
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from blog.forms import CommentForm
from django.contrib import messages


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
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()        
            messages.add_message(request, messages.SUCCESS, 'Your comment was submitted correctly.')
        else:
            messages.add_message(request, messages.ERROR, 'Your comment did not submit correctly.')
    
    now = timezone.now()
    
    # Fetch the specific post
    post = get_object_or_404(Post, id=pid, status=1, published_date__lte=now)
    
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
    comments = Comment.objects.filter(post=post.id,approved =True)
    form = CommentForm()
    context = {
        'post': post,
        'prev_post': prev_post,
        'next_post': next_post,
        'comments' : comments,
        'form'     : form,
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
    



    