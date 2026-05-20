from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import viewsets
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.permissions import IsAuthenticatedOrReadOnly

from .models import Cat
from .permissions import IsOwnerOrAdminOrReadOnly
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    """Коты пользователей Kittygram Blog: просмотр всем, управление владельцу."""

    queryset = Cat.objects.select_related("owner").all()
    serializer_class = CatSerializer
    permission_classes = (IsAuthenticatedOrReadOnly, IsOwnerOrAdminOrReadOnly)
    filter_backends = (DjangoFilterBackend, SearchFilter, OrderingFilter)
    filterset_fields = ("owner", "breed", "color")
    search_fields = ("name", "breed", "color", "owner__username")
    ordering_fields = ("name", "birth_year", "created_at", "updated_at")
    ordering = ("name",)

    def perform_create(self, serializer):
        # Владелец кота всегда берется из JWT-пользователя, а не из тела запроса.
        serializer.save(owner=self.request.user)
