from django.db.models import Count, Q
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .filters import BlogPostFilter
from .models import BlogPost, Category, Tag
from .permissions import IsAdminOrReadOnly, IsAuthorOrAdminOrReadOnly
from .serializers import BlogPostSerializer, CategorySerializer, TagSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    """Категории записей котоблога: просмотр всем, управление администратору."""

    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = (IsAdminOrReadOnly,)
    lookup_field = "pk"


class TagViewSet(viewsets.ModelViewSet):
    """Теги котоблога: просмотр всем, управление администратору."""

    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = (IsAdminOrReadOnly,)


class BlogPostViewSet(viewsets.ModelViewSet):
    """Записи котоблога с поиском, фильтрацией, сортировкой и owner-only доступом."""

    serializer_class = BlogPostSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrAdminOrReadOnly)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_class = BlogPostFilter
    search_fields = ("title", "text", "cat__name", "author__username")
    ordering_fields = ("created_at", "updated_at", "title")
    ordering = ("-created_at",)

    def get_queryset(self):
        queryset = (
            BlogPost.objects.select_related("author", "cat", "category")
            .prefetch_related("tags")
            .annotate(comments_count=Count("comments"))
        )
        user = self.request.user
        if user.is_authenticated and user.is_staff:
            return queryset
        if user.is_authenticated:
            # Автор видит свои черновики, остальные пользователи только опубликованное.
            return queryset.filter(Q(is_published=True) | Q(author=user)).distinct()
        return queryset.filter(is_published=True)

    def perform_create(self, serializer):
        # Автор записи берется из JWT-пользователя.
        serializer.save(author=self.request.user)
