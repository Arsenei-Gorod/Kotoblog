# Generated for Kittygram Blog API.

import cats.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="Cat",
            fields=[
                ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
                ("name", models.CharField(max_length=100)),
                ("breed", models.CharField(blank=True, max_length=100)),
                ("birth_year", models.PositiveIntegerField(validators=[cats.models.validate_birth_year])),
                ("color", models.CharField(blank=True, max_length=100)),
                ("description", models.TextField(blank=True)),
                ("photo", models.ImageField(blank=True, null=True, upload_to="cats/")),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("owner", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="cats", to=settings.AUTH_USER_MODEL)),
            ],
            options={"ordering": ("name",)},
        ),
    ]
