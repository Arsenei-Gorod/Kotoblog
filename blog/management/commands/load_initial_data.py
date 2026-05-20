from django.core.management.base import BaseCommand

from blog.models import Category, Tag


class Command(BaseCommand):
    help = "Создает базовые категории и теги для Kittygram Blog API."

    def handle(self, *args, **options):
        categories = [
            ("Уход", "uhod"),
            ("Питание", "pitanie"),
            ("Здоровье", "zdorovie"),
            ("Игры", "igry"),
            ("Истории", "istorii"),
            ("Советы владельцам", "sovety-vladeltsam"),
        ]
        tags = [
            ("котенок", "kotenok"),
            ("ветеринар", "veterinar"),
            ("корм", "korm"),
            ("игрушки", "igrushki"),
            ("характер", "harakter"),
            ("фотоистория", "fotoistoriya"),
        ]

        for name, slug in categories:
            Category.objects.get_or_create(name=name, slug=slug)
        for name, slug in tags:
            Tag.objects.get_or_create(name=name, slug=slug)

        self.stdout.write(self.style.SUCCESS("Базовые категории и теги созданы."))
