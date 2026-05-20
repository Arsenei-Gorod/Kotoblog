# API-примеры Kittygram Blog

Этот файл содержит практические примеры запросов и ответов для основных
сценариев Kittygram Blog API: регистрация, JWT-авторизация, создание кота,
публикация записи котоблога, фильтрация и комментарии.

## Основной сценарий

1. Пользователь регистрируется.
2. Получает JWT-токен.
3. Создает карточку своего кота.
4. Администратор создает категорию и тег.
5. Пользователь создает запись для своего кота.
6. Другие пользователи читают запись и оставляют комментарии.

## curl-примеры

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
  -d '{"name":"Мурка","birth_year":2021,"breed":"Сибирская","color":"серая"}'
```

Создание категории администратором:

```bash
curl -X POST http://localhost/api/categories/ \
  -H "Authorization: Bearer <admin_access_token>" \
  -H "Content-Type: application/json" \
  -d '{"name":"Уход","slug":"uhod","description":"Материалы об уходе за котами"}'
```

Создание тега администратором:

```bash
curl -X POST http://localhost/api/tags/ \
  -H "Authorization: Bearer <admin_access_token>" \
  -H "Content-Type: application/json" \
  -d '{"name":"корм","slug":"korm"}'
```

Создание записи котоблога:

```bash
curl -X POST http://localhost/api/posts/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{
        "cat": 1,
        "title": "Первый день Мурки",
        "text": "Сегодня Мурка впервые освоила новый дом и нашла любимую игрушку.",
        "category": 1,
        "tags": [1],
        "is_published": true
      }'
```

Добавление комментария:

```bash
curl -X POST http://localhost/api/posts/1/comments/ \
  -H "Authorization: Bearer <access_token>" \
  -H "Content-Type: application/json" \
  -d '{"text":"Отличная история, ждем продолжения!"}'
```

## Фильтрация и поиск

```bash
curl "http://localhost/api/posts/?search=корм"
curl "http://localhost/api/posts/?category=uhod"
curl "http://localhost/api/posts/?tags=kotenok"
curl "http://localhost/api/posts/?cat=1"
curl "http://localhost/api/posts/?author=arseniy"
curl "http://localhost/api/posts/?ordering=-created_at"
curl "http://localhost/api/posts/?page=2"
```

## Примеры успешных ответов

Созданный кот:

```json
{
  "id": 1,
  "owner": 1,
  "owner_username": "arseniy",
  "name": "Мурка",
  "breed": "Сибирская",
  "birth_year": 2021,
  "color": "серая",
  "description": "",
  "photo": null,
  "created_at": "2026-05-20T19:00:00+03:00",
  "updated_at": "2026-05-20T19:00:00+03:00"
}
```

Созданная запись:

```json
{
  "id": 1,
  "author": 1,
  "author_username": "arseniy",
  "cat": 1,
  "cat_name": "Мурка",
  "title": "Первый день Мурки",
  "text": "Сегодня Мурка впервые освоила новый дом и нашла любимую игрушку.",
  "image": null,
  "category": 1,
  "category_name": "Уход",
  "tags": [1],
  "tags_detail": [
    {
      "id": 1,
      "name": "корм",
      "slug": "korm"
    }
  ],
  "is_published": true,
  "comments_count": 0
}
```

## Примеры ошибок

400, запись без кота:

```json
{
  "cat": [
    "Обязательное поле."
  ]
}
```

400, короткий заголовок:

```json
{
  "title": [
    "Заголовок должен быть не короче 5 символов."
  ]
}
```

400, пустой комментарий:

```json
{
  "text": [
    "Комментарий не может быть пустым."
  ]
}
```

401, запрос без JWT-токена:

```json
{
  "detail": "Учетные данные не были предоставлены."
}
```

403, изменение чужой записи:

```json
{
  "detail": "У вас недостаточно прав для выполнения данного действия."
}
```

404, объект не найден:

```json
{
  "detail": "Страница не найдена."
}
```

405, неподдерживаемый метод:

```json
{
  "detail": "Метод \"POST\" не разрешен."
}
```

## Права доступа

- Гость может просматривать котов, записи, категории, теги и комментарии.
- Авторизованный пользователь может создавать своих котов, записи и комментарии.
- Владелец может редактировать и удалять только своих котов, записи и комментарии.
- Администратор может управлять всеми объектами.
- Категории и теги создаются, изменяются и удаляются только администратором.
