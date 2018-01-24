from django.contrib import admin

# Register your models here.
from .models import Post


class PostModelAdmin(admin.ModelAdmin):
    class Meta:
        model = Post
    list_display = ['title','__unicode__','timestamp','updated']
    list_display_links = ['__unicode__']
    list_filter = ['timestamp','updated']
    list_editable = ['title']
    search_fields = ['title','content']

admin.site.register(Post, PostModelAdmin)


