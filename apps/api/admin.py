from django.contrib import admin
from . models import Blog, Categori, HeaderLogo, Course, Wiki

class CategoriModelAdmin(admin.ModelAdmin):
    list_display = ['categori_id', 'name', 'slug', 'blog']
    prepopulated_fields = {'slug': ('name',)}
    class Meta:
        model = Categori
admin.site.register(Categori, CategoriModelAdmin)



class BlogModelAdmin(admin.ModelAdmin):
    list_display =['blog_id', 'title', 'description', 'image', 'get_created', 'updated']
    prepopulated_fields = {'slug': ('title',)}
    class Meta:
        model = Blog
admin.site.register(Blog, BlogModelAdmin)



class HeaderLogoModelAdmin(admin.ModelAdmin):
    list_display = ['name', 'image']
    class Meta:
        model = HeaderLogo
admin.site.register(HeaderLogo, HeaderLogoModelAdmin)


class CourseModelAdmin(admin.ModelAdmin):
    list_display = ['course_id', 'science', 'name']
    class Meta :
        model = Course
admin.site.register(Course, CourseModelAdmin)


class WikiModelAdmin(admin.ModelAdmin):
    list_display = ['content']
    class Meta:
        model = Wiki
admin.site.register(Wiki, WikiModelAdmin)