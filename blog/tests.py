from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from cats.models import Cat

from .models import BlogPost

User = get_user_model()


class BlogPostAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="author", password="pass12345")
        self.other_user = User.objects.create_user(username="other", password="pass12345")
        self.cat = Cat.objects.create(owner=self.user, name="Мурка", birth_year=2021)
        self.other_cat = Cat.objects.create(owner=self.other_user, name="Барсик", birth_year=2020)
        self.post = BlogPost.objects.create(
            author=self.other_user,
            cat=self.other_cat,
            title="Длинный заголовок",
            text="Это достаточно длинный текст записи котоблога.",
        )

    def valid_payload(self):
        return {
            "cat": self.cat.id,
            "title": "Новая история",
            "text": "Это достаточно длинный текст новой записи котоблога.",
        }

    def test_post_list_available_for_everyone(self):
        response = self.client.get("/api/posts/")

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_authenticated_user_can_create_post(self):
        self.client.force_authenticate(self.user)
        response = self.client.post("/api/posts/", self.valid_payload())

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(BlogPost.objects.get(title="Новая история").author, self.user)

    def test_cannot_create_post_for_another_user_cat(self):
        self.client.force_authenticate(self.user)
        payload = self.valid_payload()
        payload["cat"] = self.other_cat.id
        response = self.client.post("/api/posts/", payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_post_with_short_title(self):
        self.client.force_authenticate(self.user)
        payload = self.valid_payload()
        payload["title"] = "Кот"
        response = self.client.post("/api/posts/", payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_cannot_create_post_with_short_text(self):
        self.client.force_authenticate(self.user)
        payload = self.valid_payload()
        payload["text"] = "Коротко"
        response = self.client.post("/api/posts/", payload)

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_edit_another_user_post(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(f"/api/posts/{self.post.id}/", {"title": "Нельзя менять"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
