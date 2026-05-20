from datetime import date

from django.contrib.auth import get_user_model
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Cat

User = get_user_model()


class CatAPITests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username="owner", password="pass12345")
        self.other_user = User.objects.create_user(username="other", password="pass12345")
        self.cat = Cat.objects.create(owner=self.other_user, name="Барсик", birth_year=2020)

    def test_authenticated_user_can_create_cat(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            "/api/cats/",
            {"name": "Мурка", "birth_year": 2021, "breed": "Сибирская"},
        )

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Cat.objects.get(name="Мурка").owner, self.user)

    def test_anonymous_user_cannot_create_cat(self):
        response = self.client.post("/api/cats/", {"name": "Мурка", "birth_year": 2021})

        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_birth_year_cannot_be_future(self):
        self.client.force_authenticate(self.user)
        response = self.client.post(
            "/api/cats/",
            {"name": "Мурка", "birth_year": date.today().year + 1},
        )

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_user_cannot_edit_another_user_cat(self):
        self.client.force_authenticate(self.user)
        response = self.client.patch(f"/api/cats/{self.cat.id}/", {"name": "Чужой"})

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
