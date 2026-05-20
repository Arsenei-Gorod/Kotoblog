from django.urls import include, path

urlpatterns = [
    path("", include("cats.urls")),
    path("", include("blog.urls")),
    path("", include("comments.urls")),
]
