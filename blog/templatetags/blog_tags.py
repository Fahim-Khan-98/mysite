from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

#  Using an inclusion tag, you can render a template with context variables returned by your template tag. 

@register.inclusion_tag('blog/posts/latest_post.html')
def show_latest_posts(count=5):
    latest_post=Post.published.order_by('-publish')[:count]
    return {'latest_post': latest_post}
