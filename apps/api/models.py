from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
import uuid

from datetime import datetime


class Course(models.Model):
    PYTHON = 'Python'
    NGINX = 'Nginx'
    DATABASE = 'Database'
    SERVER = 'Server'
    SCIENCE_IN_CHOICES = (
        (PYTHON, 'Python'),
        (NGINX, 'Nginx'),
        (DATABASE, 'Database'),
        (SERVER, 'Server'),
    )

    course_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    science = models.CharField(max_length=8, choices=SCIENCE_IN_CHOICES, default=PYTHON,)
    name = models.CharField(max_length=128)

    def __str__(self):
        return f'{self.science}, {self.name}'


class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    description = models.CharField(max_length=512)
    course = models.ManyToManyField(Course)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='upload/blog/', blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.title} -  {self.description} - {self.slug}'

    class Meta:
        ordering = ['title']

    #def get_absolute_url(self):
    #    return reverse('explore_python_list', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def get_created(self):
        time = datetime.now()
        if self.created.day == time.day:
            return str(time.hour - self.created.hour) + " hours ago"
        else:
            if self.created.month == time.month:
                return str(time.day - self.created.day) + " days ago"
            else:
                if self.created.year == time.year:
                    return str(time.month - self.created.month) + " mount ago"
        return self.created


class Categori(models.Model):
    categori_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.ForeignKey(Course, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='upload/categories/', blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return f'{self.name}, {self.slug}'

    #def get_absolute_url(self):
    #    return reverse('explore_python_detail', kwargs={'blog_id': self.blog_id})

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)


class HeaderLogo(models.Model):
    name = models.ForeignKey(Course, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='upload/header_logo/', blank=True)

    def __str__(self):
        return self.name


class Wiki(models.Model):
    name = models.ForeignKey(Course, on_delete=models.CASCADE)
    content = models.TextField()

    def __str__(self):
        return self.content
