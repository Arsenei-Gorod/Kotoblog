from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import BlogPost
from cats.models import Cat

from .models import Comment

User = get_user_model()


class CommentAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="commenter", password="pass12345")
        self.other_user = User.objects.create_user(username="other", password="pass12345")
        self.cat = Cat.objects.create(owner=self.other_user, name="Барсик", birth_year=2020)
        self.post = BlogPost.objects.create(
            author=self.other_user,
            cat=self.cat,
            title="Длинный заголовок",
            text="Это достаточно длинный текст записи котоблога.",
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.other_user,
            text="Первый комментарий",
        )

    def test_comments_available_for_everyone(self):
        response = self.client.get(f"/api/posts/{self.post.id}/comments/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_comment(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            f"/api/posts/{self.post.id}/comments/",
            {"text": "Очень полезная запись."},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Comment.objects.get(text="Очень полезная запись.").author, self.user)

    def test_empty_comment_is_forbidden(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(f"/api/posts/{self.post.id}/comments/", {"text": "  "})

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_edit_another_user_comment(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(
            f"/api/comments/{self.comment.id}/",
            {"text": "Чужой комментарий"},
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
