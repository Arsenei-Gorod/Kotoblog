from datetime import date

from rest_framework import serializers

from .models import Cat


class CatSerializer(serializers.ModelSerializer):
    owner_username = serializers.CharField(source="owner.username", read_only=True)

    class Meta:
        model = Cat
        fields = (
            "id",
            "owner",
            "owner_username",
            "name",
            "breed",
            "birth_year",
            "color",
            "description",
            "photo",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("owner", "owner_username", "created_at", "updated_at")

    def validate_name(self, value):
        if not value.strip():
            raise serializers.ValidationError("Имя кота обязательно.")
        return value

    def validate_birth_year(self, value):
        if value > date.today().year:
            raise serializers.ValidationError(
                "Год рождения не может быть больше текущего года."
            )
        return value
