from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from .models import Post
from .forms import PostForm


# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
    context = {
        'form': form,
    }

    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        print title
        print content

    return render(request, 'post_form.html', context)


def post_detail(request, post_id):
    instance = get_object_or_404(Post, id=post_id)

    context = {
        'title': 'detail',
        'instance': instance,
    }
    return render(request, 'post_detail.html', context)


def post_list(request):
    instance = Post.objects.all()

    context = {
        'title': 'List',
        'objects_list': instance,
    }

    return render(request, 'index.html', context)


def post_update(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=instance)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()

    context = {
        'title': 'detail',
        'instance': instance,
        'form': form,
    }

    return render(request, 'post_detail.html', context)
