from rest_framework import serializers

from .models import Comment


class CommentSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)

    class Meta:
        model = Comment
        fields = (
            "id",
            "post",
            "author",
            "author_username",
            "text",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "post",
            "author",
            "author_username",
            "created_at",
            "updated_at",
        )

    def validate_text(self, value):
        if not value.strip():
            raise serializers.ValidationError("Комментарий не может быть пустым.")
        return value
