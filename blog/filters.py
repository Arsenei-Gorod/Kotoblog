import django_filters

from .models import BlogPost


class BlogPostFilter(django_filters.FilterSet):
    category = django_filters.CharFilter(field_name="category__slug")
    tags = django_filters.CharFilter(field_name="tags__slug")
    cat = django_filters.NumberFilter(field_name="cat__id")
    author = django_filters.CharFilter(field_name="author__username")

    class Meta:
        model = BlogPost
        fields = ("category", "tags", "cat", "author", "is_published")
