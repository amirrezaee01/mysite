from django import template
register = template.Library()
from blog.models import Post
from blog.models import Catagory


@register.simple_tag(name='totalpost')
def function():
    posts = Post.objects.filter(status=1).count()
    return posts

@register.simple_tag(name='posts')
def function():
    posts = Post.objects.filter(status=1)
    return posts

@register.filter
def sinppet(value,arg=50):
    return value[:arg]

@register.inclusion_tag('blog/blog-popular-post.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('-published_date')#[:3]
    return{'posts':posts}

@register.inclusion_tag('blog/blog-post-categories.html')
def postcategories():
    posts = Post.objects.filter(status=1)
    categories = Catagory.objects.all()
    cat_dict = {}
    for name in categories:
        cat_dict[name]=posts.filter(category=name).count()
    return {"categories":cat_dict}