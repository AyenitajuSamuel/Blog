from django.contrib import admin
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date_created', 'date_updated']
    search_fields = ['title', 'content']
