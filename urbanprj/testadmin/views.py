from django.shortcuts import render
from django.core.paginator import Paginator
from .models import Post


def my_post_list(request):
    posts = Post.objects.all()
    numposts = request.GET.get('numposts')
    if numposts is None:
        numposts = 3
    else:
        numposts = int(numposts)
    paginator = Paginator(posts, per_page=numposts)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    num_pages_list = [num for num in range(1, 21)]
    context = {
        'numposts': numposts,
        'page_posts': page_posts,
        'num_pages_list': num_pages_list
    }
    return render(request, 'my_post_list.html', context=context)


def post_list(request):
    posts = Post.objects.all()
    paginator = Paginator(posts, 3)
    page_number = request.GET.get('page')
    page_posts = paginator.get_page(page_number)
    return render(request, 'post_list.html', {'page_posts': page_posts})
