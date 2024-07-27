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
    # Retrieve all posts with status 1 (published)
    posts = Post.objects.filter(status=1)
    
    # Retrieve all categories
    categories = Catagory.objects.all()
    
    # Initialize an empty dictionary to store category names and their corresponding post counts
    cat_dict = {}
    
    # Iterate through each category
    for name in categories:
        # Filter the posts queryset by the current category
        filtered_posts = posts.filter(category=name)
        
        # Count the number of posts in the filtered queryset
        count = filtered_posts.count()
        
        # Add the category and its post count to the dictionary
        cat_dict[name] = count
    
    # Return the dictionary of categories and post counts to the template
    return {"categories": cat_dict}