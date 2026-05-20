from django.urls import path
from rest_framework.routers import DefaultRouter

from .views import CommentDetailViewSet, CommentViewSet

router = DefaultRouter()
router.register("comments", CommentDetailViewSet, basename="comments")

urlpatterns = [
    path(
        "posts/<int:post_id>/comments/",
        CommentViewSet.as_view({"get": "list", "post": "create"}),
        name="post-comments",
    ),
]
urlpatterns += router.urls
