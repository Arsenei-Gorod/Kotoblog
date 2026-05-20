from django.shortcuts import get_object_or_404
from rest_framework import mixins, viewsets
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from blog.models import BlogPost

from .models import Comment
from .permissions import IsAuthorOrAdminOrReadOnly
from .serializers import CommentSerializer


class CommentViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """Комментарии к записи котоблога: список всем, создание авторизованным."""

    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrAdminOrReadOnly)

    def get_queryset(self):
        queryset = Comment.objects.select_related("author", "post")
        post_id = self.kwargs.get("post_id")
        if post_id:
            # Nested-роут показывает комментарии только выбранной записи.
            return queryset.filter(post_id=post_id)
        return queryset

    def perform_create(self, serializer):
        post = get_object_or_404(BlogPost, id=self.kwargs.get("post_id"))
        # Автор и запись берутся из контекста запроса, а не из тела.
        serializer.save(author=self.request.user, post=post)


class CommentDetailViewSet(
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet,
):
    """Отдельный роут для просмотра, редактирования и удаления комментария."""

    queryset = Comment.objects.select_related("author", "post")
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsAuthorOrAdminOrReadOnly)
