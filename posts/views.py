from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def post_home(request):
    return HttpResponse("<h>Hello</h>")
def post_create(request):
    return HttpResponse("<h>create</h>")

def post_list(request):
    return render(request, 'index.html',{})
