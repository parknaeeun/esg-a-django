from django.shortcuts import render
from .models import Post


def index(request):
    #전체 포스팅을 가져올 준비. 아직은 안 가져옴.
    post_qs = Post.objects.all().order_by("-pk")

    return render(request, 'blog/index.html',
    {'posts_list':post_qs})

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single_post_page.html',
    {"post":post})