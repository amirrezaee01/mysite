from django import template
register = template.Library()
from blog.models import Post   

@register.inclusion_tag('website/latest_post.html')
def latestpost():
    posts = Post.objects.filter(status=1).order_by('published_date')#[:3]
    return{'posts':posts}