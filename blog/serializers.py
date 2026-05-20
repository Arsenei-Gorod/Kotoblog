from rest_framework import serializers

from cats.models import Cat

from .models import BlogPost, Category, Tag


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ("id", "name", "slug", "description")


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ("id", "name", "slug")


class BlogPostSerializer(serializers.ModelSerializer):
    author_username = serializers.CharField(source="author.username", read_only=True)
    cat_name = serializers.CharField(source="cat.name", read_only=True)
    category_name = serializers.CharField(source="category.name", read_only=True)
    tags_detail = TagSerializer(source="tags", many=True, read_only=True)
    comments_count = serializers.IntegerField(read_only=True)

    class Meta:
        model = BlogPost
        fields = (
            "id",
            "author",
            "author_username",
            "cat",
            "cat_name",
            "title",
            "text",
            "image",
            "category",
            "category_name",
            "tags",
            "tags_detail",
            "is_published",
            "comments_count",
            "created_at",
            "updated_at",
        )
        read_only_fields = (
            "author",
            "author_username",
            "cat_name",
            "category_name",
            "tags_detail",
            "comments_count",
            "created_at",
            "updated_at",
        )

    def validate_title(self, value):
        if len(value.strip()) < 5:
            raise serializers.ValidationError(
                "Заголовок должен быть не короче 5 символов."
            )
        return value

    def validate_text(self, value):
        if len(value.strip()) < 20:
            raise serializers.ValidationError(
                "Текст записи должен быть не короче 20 символов."
            )
        return value

    def validate(self, data):
        # Проверяем кота на уровне сериализатора, чтобы API вернул понятную 400-ошибку.
        request = self.context.get("request")
        cat = data.get("cat") or getattr(self.instance, "cat", None)
        if request and request.method == "POST" and not cat:
            raise serializers.ValidationError({"cat": "Нужно выбрать кота для записи."})
        if request and cat and not request.user.is_staff:
            if not Cat.objects.filter(id=cat.id, owner=request.user).exists():
                raise serializers.ValidationError(
                    {"cat": "Можно создать запись только для своего кота."}
                )
        return data
