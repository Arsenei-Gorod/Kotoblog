from datetime import date

from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError
from django.db import models

User = get_user_model()


def validate_birth_year(value):
    if value > date.today().year:
        raise ValidationError("Год рождения не может быть больше текущего года.")


class Cat(models.Model):
    owner = models.ForeignKey(User, related_name="cats", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    breed = models.CharField(max_length=100, blank=True)
    birth_year = models.PositiveIntegerField(validators=[validate_birth_year])
    color = models.CharField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    photo = models.ImageField(upload_to="cats/", blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ("name",)

    def __str__(self):
        return self.name
