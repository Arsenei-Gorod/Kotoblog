# Kittygram Blog API

## Описание проекта
Kittygram Blog API — REST API-сервис для ведения котоблога в рамках проекта Kittygram. Пользователи могут регистрироваться, создавать карточки своих котов, публиковать записи, добавлять категории, теги и комментарии, искать и фильтровать контент.

## Возможности
- регистрация и JWT-авторизация;
- создание карточек котов;
- создание записей котоблога;
- категории и теги;
- комментарии;
- поиск;
- фильтрация;
- сортировка;
- пагинация;
- права доступа owner-only;
- Swagger и Redoc;
- Docker-развертывание.

## Стек технологий
Python 3.11, Django, Django REST Framework, PostgreSQL, Docker, Docker Compose, Nginx, Gunicorn, Simple JWT, Djoser, drf-spectacular, django-filter, Pillow.

## Структура проекта
```text
kittygram_blog/
├── manage.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── nginx.conf
├── .env.example
├── kittygram_blog/
├── cats/
├── blog/
├── comments/
├── api/
├── docs/
│   ├── api_endpoints.md
│   ├── api_examples.md
│   ├── deployment.md
│   ├── deployment_diagram.md
│   ├── diagrams.md
│   ├── postman_requests.md
│   ├── use_case_diagram.md
│   └── postman/
│       └── kittygram_blog.postman_collection.json
├── README.md
└── .gitignore
```

## Переменные окружения
Файл `.env.example` содержит пример:

| Переменная | Назначение |
| --- | --- |
| `SECRET_KEY` | секретный ключ Django |
| `DEBUG` | режим отладки: `True` или `False` |
| `ALLOWED_HOSTS` | список разрешенных хостов через запятую |
| `POSTGRES_DB` | имя базы данных PostgreSQL |
| `POSTGRES_USER` | пользователь PostgreSQL |
| `POSTGRES_PASSWORD` | пароль PostgreSQL |
| `DB_HOST` | хост базы данных |
| `DB_PORT` | порт базы данных |

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

Локальные адреса при запуске через `runserver`:

| Адрес | Описание |
| --- | --- |
| `http://127.0.0.1:8000/api/posts/` | записи котоблога |
| `http://127.0.0.1:8000/api/cats/` | коты |
| `http://127.0.0.1:8000/api/schema/` | OpenAPI-схема |
| `http://127.0.0.1:8000/api/docs/swagger/` | Swagger |
| `http://127.0.0.1:8000/api/docs/redoc/` | Redoc |
| `http://127.0.0.1:8000/admin/` | админ-панель |

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

## Запуск через Docker
```bash
cp .env.example .env
docker compose up -d --build
docker compose exec backend python manage.py migrate
docker compose exec backend python manage.py createsuperuser
docker compose exec backend python manage.py load_initial_data
```

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

## Проверка API
- http://localhost/api/posts/
- http://localhost/api/docs/swagger/
- http://localhost/api/docs/redoc/

## Основные эндпоинты
| URL | Метод | Назначение | Права доступа | Тело запроса | Коды ответов |
| --- | --- | --- | --- | --- | --- |
| `/api/auth/users/` | POST | регистрация | все | `username`, `password` | 201, 400 |
| `/api/auth/jwt/create/` | POST | получение JWT | все | `username`, `password` | 200, 401 |
| `/api/auth/jwt/refresh/` | POST | обновление JWT | все | `refresh` | 200, 401 |
| `/api/auth/jwt/verify/` | POST | проверка JWT | все | `token` | 200, 401 |
| `/api/auth/users/me/` | GET | текущий пользователь | авторизованный | нет | 200, 401 |
| `/api/cats/` | GET, POST | список и создание котов | чтение всем, создание авторизованным | `name`, `birth_year` | 200, 201, 400, 401 |
| `/api/cats/{id}/` | GET, PATCH, DELETE | кот | чтение всем, изменение владельцу или админу | поля кота | 200, 403, 404 |
| `/api/posts/` | GET, POST | список и создание записей | чтение всем, создание авторизованным | `cat`, `title`, `text` | 200, 201, 400, 401 |
| `/api/posts/{id}/` | GET, PATCH, DELETE | запись | чтение всем, изменение автору или админу | поля записи | 200, 403, 404 |
| `/api/categories/` | GET, POST | категории | чтение всем, изменение админу | `name`, `slug` | 200, 201, 403 |
| `/api/tags/` | GET, POST | теги | чтение всем, изменение админу | `name`, `slug` | 200, 201, 403 |
| `/api/posts/{post_id}/comments/` | GET, POST | комментарии записи | чтение всем, создание авторизованным | `text` | 200, 201, 400, 401 |
| `/api/comments/{id}/` | GET, PATCH, DELETE | комментарий | чтение всем, изменение автору или админу | `text` | 200, 403, 404 |
| `/api/schema/` | GET | OpenAPI-схема | все | нет | 200 |
| `/api/docs/swagger/` | GET | Swagger UI | все | нет | 200 |
| `/api/docs/redoc/` | GET | Redoc | все | нет | 200 |

## Примеры запросов
Регистрация:
```bash
curl -X POST http://localhost/api/auth/users/ \
  -H "Content-Type: application/json" \
  -d '{"username":"arseniy","password":"StrongPass123"}'
```

Получение токена:
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
  -d '{"cat":1,"title":"Первый день Мурки","text":"Сегодня Мурка впервые освоила новый дом и нашла любимую игрушку."}'
```

Добавление комментария:
```bash
curl -X POST http://localhost/api/posts/1/comments/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"text":"Отличная история, ждем продолжения!"}'
```

Поиск записи:
```bash
curl "http://localhost/api/posts/?search=корм"
```

## Postman
Коллекция находится в `docs/postman/kittygram_blog.postman_collection.json`.

Перед запуском коллекции создай суперпользователя и проверь переменные `admin_username` и `admin_password`. Запросы категорий и тегов используют `admin_access_token`, а кот, запись и комментарий создаются обычным пользователем через `access_token`. Негативный сценарий изменения чужой записи использует отдельный `second_access_token`.

## Дополнительная документация
- `docs/api_endpoints.md` — полная таблица endpoint'ов.
- `docs/api_examples.md` — curl-примеры, успешные ответы и ошибки.
- `docs/postman_requests.md` — список запросов Postman-коллекции.
- `docs/deployment.md` — описание Docker-развертывания.
- `docs/use_case_diagram.md` — Mermaid Use Case Diagram.
- `docs/deployment_diagram.md` — Mermaid Deployment Diagram.
- `docs/diagrams.md` — краткое текстовое описание диаграмм для курсовой.

## Тестирование
```bash
docker compose exec backend python manage.py test
```

## Автор
Арсений Городский
