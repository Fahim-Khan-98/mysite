from django.contrib import admin
from .models import Post
# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'status', 'publish']
    list_filter = [ 'author', 'slug', 'status', 'publish', 'created']
    search_fields = ['title', 'author']
    prepopulated_fields = { 'slug':('title',)}
    raw_id_fields = ['author']
    date_hierarchy = 'publish'
    ordering = ['status', 'publish']