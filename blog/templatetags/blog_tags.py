from django.utils.safestring import mark_safe
import markdown
from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()

@register.simple_tag
def total_posts():
    return Post.published.count()

#  Using an inclusion tag, you can render a template with context variables returned by your template tag. 

@register.inclusion_tag('blog/posts/latest_posts.html')
def show_latest_posts(count=5):
 latest_posts = Post.published.order_by('-publish')[:count]
 return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
   # Assuming you want to find the post with the maximum total number of comments
   return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
    


# @register.inclusion_tag('blog/posts/most_commented_post.html')
# def get_most_commented_posts(count=5):
#    # Assuming you want to find the post with the maximum total number of comments
#    post_with_max_comments = Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]
#    return {'post_with_max_comments': post_with_max_comments}



@register.filter(name='markdown')
def markdown_format(text):
   return mark_safe(markdown.markdown(text))