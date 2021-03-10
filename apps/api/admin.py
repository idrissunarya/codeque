from django.contrib import admin
from . models import Blog

class BlogModelAdmin(admin.ModelAdmin):
    list_display =['blog_id', 'title', 'tag', 'description', 'image', 'created', 'updated']
    class Meta:
        model = Blog
admin.site.register(Blog, BlogModelAdmin)
