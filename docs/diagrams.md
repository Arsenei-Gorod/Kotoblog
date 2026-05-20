# Диаграммы для курсовой

Этот файл дублирует диаграммы в кратком описательном формате. Mermaid-версии
находятся в `docs/use_case_diagram.md` и `docs/deployment_diagram.md`.

## Use Case Diagram

Акторы:

- Гость
- Пользователь
- Владелец объекта
- Администратор

Use case:

- Просмотреть список записей.
- Просмотреть список котов.
- Зарегистрироваться.
- Авторизоваться.
- Создать кота.
- Изменить своего кота.
- Создать запись котоблога.
- Изменить свою запись.
- Удалить свою запись.
- Добавить комментарий.
- Изменить свой комментарий.
- Управлять категориями.
- Управлять тегами.
- Управлять всеми объектами через админ-панель.

Описание связей:

- Гость просматривает публичные списки котов, записей, категорий, тегов и комментариев.
- Пользователь создает котов, записи и комментарии.
- Владелец объекта изменяет и удаляет только свои объекты.
- Администратор управляет всеми объектами и справочниками.

## Deployment Diagram

Узлы:

- `Client / Postman`
- `Nginx container`
- `Backend container: Django REST Framework + Gunicorn`
- `PostgreSQL container`
- `static_value volume`
- `media_value volume`
- `postgres_data volume`

Связи:

- `Client -> Nginx`: HTTP port 80.
- `Nginx -> Backend`: HTTP proxy to port 8000.
- `Backend -> PostgreSQL`: database connection through Django ORM.
- `Backend -> static_value`: static files.
- `Backend -> media_value`: uploaded images.
- `PostgreSQL -> postgres_data`: persistent database data.
