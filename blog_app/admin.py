from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'body', 'date_added')
    list_filter = ('date_added',)
    search_fields = ('title', 'content')
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
