import django_filters
from .models import Post

class PostFilter(django_filters.Filter):
    class Meta:
        model = Post
        filter = 'title'