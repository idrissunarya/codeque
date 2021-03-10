from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Blog

class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = ['blog_id', 'title', 'tag', 'description', 'content', 'created', 'updated']