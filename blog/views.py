from django.shortcuts import render, get_object_or_404
from django.http import Http404
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import Post
# Create your views here.




def post_list(request):
    post_list = Post.objects.all()
    # Pagination with 3 posts per page
    paginator = Paginator(post_list,3)
    page_number = request.GET.get('page',1)
    try:
        posts = paginator.page(page_number)
    except PageNotAnInteger:
        # If page_number is not an integer deliver the first page
        posts = paginator.page(1)

    except EmptyPage:
         # If page_number is out of range deliver last page of results
         posts = paginator.page(paginator.num_pages)
    context={
        'posts' : posts
    }
    return render(request, 'blog/post_list.html', context)



def post_detail(request, id):
    post = get_object_or_404(Post, id=id, status=Post.Status.PUBLISHED)
    context={
        'post' : post,

    }
    return render(request,'blog/post_detail.html',context)

