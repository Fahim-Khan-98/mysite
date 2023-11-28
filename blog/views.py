from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.views.generic import ListView
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
from .forms import EmailPostForm
from django.conf import settings
from django.core.mail import send_mail
# Create your views here.


def post_share(request, post_id):
    posts = get_object_or_404(Post, id = post_id, status=Post.Status.PUBLISHED)
    sent=False
    form = EmailPostForm() 

    if request.method == 'POST':
        #form was submitted
        form = EmailPostForm(request.POST)
        if form.is_valid():
            # Form fields passed validation
            cd = form.cleaned_data
            post_url = request.build_absolute_uri(posts.get_absolute_url())
            subject = f"{cd['name']} recomands you to read {posts.title}"
            message = f" read {posts.title} at {post_url} \n\n" \
                       f"{cd['name']}\'s comments :  {cd['comments']}"
            send_mail(subject, message, 'fahim.khancsebd@gmail.com', [cd['to']])
            sent = True

    context={
        'posts' : posts,
        'form' : form,
        'sent' : sent

         }
    return render(request, 'blog/posts/share.html', context)

# def post_list(request):
#     post_list = Post.objects.all()
#     # Pagination with 3 posts per page
#     paginator = Paginator(post_list,3)
#     page_number = request.GET.get('page',1)
#     try:
#         posts = paginator.page(page_number)
#     except PageNotAnInteger:
#         # If page_number is not an integer deliver the first page
#         posts = paginator.page(1)

#     except EmptyPage:
#          # If page_number is out of range deliver last page of results
#          posts = paginator.page(paginator.num_pages)
#     context={
#         'posts' : posts
#     }
#     return render(request, 'blog/post_list.html', context)


class PostListView(ListView):
    
    model = Post
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post_list.html'

    def get_queryset(self):
        queryset = Post.objects.all()
        return queryset



def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context={
        'post' : post,

    }
    return render(request,'blog/post_detail.html',context)

