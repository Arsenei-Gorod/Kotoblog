# Развертывание Kittygram Blog API

## Docker-архитектура

- `Client / Postman`: браузер или Postman отправляет HTTP-запросы.
- `nginx`: принимает запросы на порту 80 и проксирует API в backend.
- `backend`: Django REST Framework + Gunicorn на порту 8000.
- `db`: PostgreSQL на порту 5432.
- `postgres_data`: volume для постоянного хранения базы данных.
- `static_value`: volume для собранных статических файлов.
- `media_value`: volume для пользовательских изображений.

Связи:

- `Client -> Nginx`: HTTP port 80.
- `Nginx -> Backend`: proxy_pass на `backend:8000`.
- `Backend -> PostgreSQL`: подключение через Django ORM.
- `Backend -> static_value`: сборка статики через `collectstatic`.
- `Backend -> media_value`: хранение фотографий котов и изображений записей.
- `PostgreSQL -> postgres_data`: постоянное хранение данных.

## Команды запуска

```bash
git clone https://github.com/Arsenei-Gorod/Kotoblog.git
cd Kotoblog
cp .env.example .env
docker compose up -d --build
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py load_initial_data
```

## Команды проверки

```bash
docker compose ps
docker compose logs -f backend
docker compose logs -f nginx
docker compose exec backend python manage.py test
docker compose exec backend python manage.py spectacular --file /tmp/schema.yaml
```

## Адреса проверки

- `http://localhost/api/posts/`
- `http://localhost/api/cats/`
- `http://localhost/api/categories/`
- `http://localhost/api/tags/`
- `http://localhost/api/schema/`
- `http://localhost/api/docs/swagger/`
- `http://localhost/api/docs/redoc/`
- `http://localhost/admin/`

## Остановка и перезапуск

```bash
docker compose stop
docker compose start
docker compose down
docker compose up -d --build
```

Чтобы удалить базу и volumes полностью:

```bash
docker compose down -v
```
