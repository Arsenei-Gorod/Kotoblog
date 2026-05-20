from rest_framework.routers import DefaultRouter

from .views import BlogPostViewSet, CategoryViewSet, TagViewSet

router = DefaultRouter()
router.register("posts", BlogPostViewSet, basename="posts")
router.register("categories", CategoryViewSet, basename="categories")
router.register("tags", TagViewSet, basename="tags")

urlpatterns = router.urls
