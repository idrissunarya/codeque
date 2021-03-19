from django.contrib import admin
from . models import Blog, Categori

class CategoriModelAdmin(admin.ModelAdmin):
    list_display = ['categori_id', 'name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = Categori
admin.site.register(Categori, CategoriModelAdmin)



class BlogModelAdmin(admin.ModelAdmin):
    list_display =['blog_id', 'title', 'description', 'image', 'created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Blog
admin.site.register(Blog, BlogModelAdmin)