from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid


class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='upload/blog/', blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.title} {self.description}'

    class Meta:
        ordering = ['title']

    def get_absolute_url(self):
        return reverse('explore_python_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)


class Categori(models.Model):
    categori_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=64)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='upload/categories/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.name

    #def get_absolute_url(self):
    #    return reverse('explore_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)
