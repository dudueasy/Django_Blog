from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from .models import Post
from .forms import PostForm


# Create your views here.

def post_create(request):
    form = PostForm(request.POST or None)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post Successfully Created')

        return HttpResponseRedirect(instance.get_absolute_url())
    else:
        messages.error(request, 'Fail to Create Post')

    context = {
        'form': form,
    }
    # return a HTML <form> for get method
    # (while variable form.is_valid fail)
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

    return render(request, 'post_list.html', context)


def post_update(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    form = PostForm(request.POST or None, instance=instance)

    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        messages.success(request, 'Post Successfully Updated', extra_tags='extra_tag')

        return HttpResponseRedirect(instance.get_absolute_url())
    # else:
    #     # messages.error(request, 'Fail to Update Post')

    context = {
        'title': 'detail',
        'instance': instance,
        'form': form,
    }

    return render(request, 'post_form.html', context)


def post_delete(request, post_id=None):
    instance = get_object_or_404(Post, id=post_id)
    instance.delete()
    messages.success(request, 'Post Successfully Deleted')

    return redirect("posts:list")
