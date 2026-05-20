# Kittygram Blog API

## Описание проекта

**Kittygram Blog API** — учебный REST API-сервис для ведения котоблога в рамках проекта Kittygram.

Проект разработан для курсовой работы по теме:  
**«Разработка и развертывание REST API-сервиса для ведения котоблога в рамках проекта Kittygram на основе Django Rest Framework»**.

Сервис позволяет пользователям регистрироваться, создавать карточки своих котов, публиковать записи котоблога, добавлять категории и теги, комментировать записи, искать и фильтровать контент. Пользователь может изменять и удалять только свои объекты, а администратор может управлять всеми данными через API и Django admin.

## Возможности проекта

- регистрация пользователей;
- JWT-авторизация;
- создание карточек котов;
- редактирование и удаление только своих котов;
- создание записей котоблога;
- редактирование и удаление только своих записей;
- категории и теги для записей;
- комментарии к записям;
- редактирование и удаление только своих комментариев;
- поиск по записям;
- фильтрация по категории, тегу, коту, автору и статусу публикации;
- сортировка записей;
- пагинация;
- разграничение прав доступа;
- Swagger и Redoc;
- Docker-развертывание;
- PostgreSQL;
- Nginx и Gunicorn;
- Postman-коллекция для проверки API;
- Mermaid-диаграммы в `docs`.

## Стек технологий

- Python 3.11+
- Django
- Django REST Framework
- Djoser
- Simple JWT
- drf-spectacular
- django-filter
- Pillow
- PostgreSQL
- Docker
- Docker Compose
- Gunicorn
- Nginx
- Postman
- Swagger / Redoc

## Структура проекта

```text
kittygram_blog/
├── api/
│   ├── pagination.py
│   └── urls.py
├── blog/
│   ├── management/
│   │   └── commands/
│   │       └── load_initial_data.py
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── admin.py
│   ├── filters.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── cats/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── admin.py
│   ├── filters.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── comments/
│   ├── migrations/
│   │   └── 0001_initial.py
│   ├── admin.py
│   ├── models.py
│   ├── permissions.py
│   ├── serializers.py
│   ├── tests.py
│   ├── urls.py
│   └── views.py
├── docs/
│   ├── postman/
│   │   └── kittygram_blog.postman_collection.json
│   ├── api_endpoints.md
│   ├── api_examples.md
│   ├── deployment.md
│   ├── deployment_diagram.md
│   ├── diagrams.md
│   ├── postman_requests.md
│   └── use_case_diagram.md
├── kittygram_blog/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
├── docker-compose.yml
├── manage.py
├── nginx.conf
└── requirements.txt
```

Дополнительные материалы находятся в каталоге `docs/`:

- `docs/api_endpoints.md` — полная таблица API-эндпоинтов;
- `docs/api_examples.md` — примеры запросов и ответов;
- `docs/deployment.md` — описание Docker-развертывания;
- `docs/postman_requests.md` — описание проверочных Postman-запросов;
- `docs/use_case_diagram.md` — Mermaid Use Case Diagram;
- `docs/deployment_diagram.md` — Mermaid Deployment Diagram;
- `docs/diagrams.md` — краткое описание диаграмм;
- `docs/postman/kittygram_blog.postman_collection.json` — Postman-коллекция.

## Переменные окружения

Перед запуском через Docker создай файл `.env` на основе `.env.example`:

```bash
cp .env.example .env
```

Пример переменных:

```env
SECRET_KEY=django-insecure-kittygram-blog-secret-key-for-local-development
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1,0.0.0.0
POSTGRES_DB=kittygram_blog
POSTGRES_USER=kittygram_user
POSTGRES_PASSWORD=kittygram_password
DB_HOST=db
DB_PORT=5432
```

| Переменная | Назначение |
| --- | --- |
| `SECRET_KEY` | секретный ключ Django |
| `DEBUG` | режим отладки |
| `ALLOWED_HOSTS` | разрешенные хосты через запятую |
| `POSTGRES_DB` | имя базы данных PostgreSQL |
| `POSTGRES_USER` | пользователь PostgreSQL |
| `POSTGRES_PASSWORD` | пароль PostgreSQL |
| `DB_HOST` | хост базы данных |
| `DB_PORT` | порт базы данных |

## Запуск через Docker

```bash
cp .env.example .env
docker compose up -d --build
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py load_initial_data
```

После запуска API будет доступен по адресу:

- `http://localhost/api/posts/`
- `http://localhost/api/cats/`
- `http://localhost/api/categories/`
- `http://localhost/api/tags/`
- `http://localhost/admin/`

Документация API:

- `http://localhost/api/schema/`
- `http://localhost/api/docs/swagger/`
- `http://localhost/api/docs/redoc/`

Полезные команды Docker:

```bash
docker compose ps
docker compose logs -f backend
docker compose logs -f nginx
docker compose stop
docker compose start
docker compose down
docker compose up -d --build
```

## Локальный запуск Linux / macOS

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py load_initial_data
python manage.py runserver
```

Локальные адреса:

- `http://127.0.0.1:8000/api/posts/`
- `http://127.0.0.1:8000/api/docs/swagger/`
- `http://127.0.0.1:8000/api/docs/redoc/`
- `http://127.0.0.1:8000/admin/`

## Локальный запуск Windows PowerShell

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py load_initial_data
python manage.py runserver
```

## Основные эндпоинты

| URL | Метод | Назначение | Права доступа |
| --- | --- | --- | --- |
| `/api/auth/users/` | POST | регистрация пользователя | все |
| `/api/auth/jwt/create/` | POST | получение JWT-токена | все |
| `/api/auth/jwt/refresh/` | POST | обновление JWT-токена | все |
| `/api/auth/jwt/verify/` | POST | проверка JWT-токена | все |
| `/api/auth/users/me/` | GET | текущий пользователь | авторизованный |
| `/api/cats/` | GET | список котов | все |
| `/api/cats/` | POST | создание кота | авторизованный |
| `/api/cats/{id}/` | GET | детали кота | все |
| `/api/cats/{id}/` | PATCH, DELETE | изменение или удаление кота | владелец или админ |
| `/api/posts/` | GET | список записей | все |
| `/api/posts/` | POST | создание записи | авторизованный |
| `/api/posts/{id}/` | GET | детали записи | все |
| `/api/posts/{id}/` | PATCH, DELETE | изменение или удаление записи | автор или админ |
| `/api/categories/` | GET | список категорий | все |
| `/api/categories/` | POST | создание категории | админ |
| `/api/tags/` | GET | список тегов | все |
| `/api/tags/` | POST | создание тега | админ |
| `/api/posts/{post_id}/comments/` | GET | комментарии записи | все |
| `/api/posts/{post_id}/comments/` | POST | создание комментария | авторизованный |
| `/api/comments/{id}/` | GET | детали комментария | все |
| `/api/comments/{id}/` | PATCH, DELETE | изменение или удаление комментария | автор или админ |
| `/api/schema/` | GET | OpenAPI-схема | все |
| `/api/docs/swagger/` | GET | Swagger UI | все |
| `/api/docs/redoc/` | GET | Redoc | все |

## Примеры запросов

Регистрация пользователя:

```bash
curl -X POST http://localhost/api/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"arseniy","password":"StrongPass123"}'
```

Получение JWT-токена:

```bash
curl -X POST http://localhost/api/auth/jwt/create/ \
  -H "Content-Type: application/json" \
  -d '{"username":"arseniy","password":"StrongPass123"}'
```

Создание кота:

```bash
curl -X POST http://localhost/api/cats/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Мурка","breed":"Сибирская","birth_year":2021,"color":"серая"}'
```

Создание записи:

```bash
curl -X POST http://localhost/api/posts/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"cat":1,"title":"Первый день Мурки","text":"Сегодня Мурка впервые освоила новый дом и нашла любимую игрушку.","category":1,"tags":[1]}'
```

Добавление комментария:

```bash
curl -X POST http://localhost/api/posts/1/comments/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"text":"Отличная история, ждем продолжения!"}'
```

Поиск и фильтрация:

```bash
curl "http://localhost/api/posts/?search=корм"
curl "http://localhost/api/posts/?category=uhod"
curl "http://localhost/api/posts/?tags=kotenok"
curl "http://localhost/api/posts/?cat=1"
curl "http://localhost/api/posts/?author=arseniy"
curl "http://localhost/api/posts/?ordering=-created_at"
```

## Postman

Postman-коллекция находится здесь:

```text
docs/postman/kittygram_blog.postman_collection.json
```

Перед запуском коллекции:

1. Создай суперпользователя.
2. Проверь переменные `admin_username` и `admin_password`.
3. Запускай запросы последовательно.

Категории и теги создаются через `admin_access_token`. Кот, запись и комментарий создаются обычным пользователем через `access_token`. Негативный сценарий изменения чужой записи использует `second_access_token`.

## Тестирование

Через Docker:

```bash
docker compose exec backend python manage.py test
```

Локально:

```bash
python manage.py test
```

## Начальное наполнение

Команда:

```bash
python manage.py load_initial_data
```

Создает базовые категории:

- Уход
- Питание
- Здоровье
- Игры
- Истории
- Советы владельцам

И базовые теги:

- котенок
- ветеринар
- корм
- игрушки
- характер
- фотоистория

## Автор

Арсений Городский
