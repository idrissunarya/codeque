from django.db import models
import uuid


class Blog(models.Model):
    blog_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=256)
    tag = models.CharField(max_length=64)
    description = models.CharField(max_length=512)
    image = models.ImageField(upload_to='upload/blog', blank=True)
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)

    def __str__(self):
        return self.title