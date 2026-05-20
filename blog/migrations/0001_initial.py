# Generated for Kittygram Blog API.

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cats", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=120, unique=True)),
                ("description", models.TextField(blank=True)),
            ],
            options={"verbose_name": "Категория", "verbose_name_plural": "Категории", "ordering": ("name",)},
        ),
        migrations.CreateModel(
            name="Tag",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100, unique=True)),
                ("slug", models.SlugField(max_length=120, unique=True)),
            ],
            options={"verbose_name": "Тег", "verbose_name_plural": "Теги", "ordering": ("name",)},
        ),
        migrations.CreateModel(
            name="BlogPost",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("title", models.CharField(max_length=200)),
                ("text", models.TextField()),
                ("image", models.ImageField(blank=True, null=True, upload_to="posts/")),
                ("is_published", models.BooleanField(default=True)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("author", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="posts", to=settings.AUTH_USER_MODEL)),
                ("cat", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="posts", to="cats.cat")),
                ("category", models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name="posts", to="blog.category")),
                ("tags", models.ManyToManyField(blank=True, related_name="posts", to="blog.tag")),
            ],
            options={"verbose_name": "Запись котоблога", "verbose_name_plural": "Записи котоблога", "ordering": ("-created_at",)},
        ),
    ]
