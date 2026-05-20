# API Endpoints

Таблица соответствует реальным маршрутам DRF routers, Djoser и drf-spectacular.

| № | URL | Метод | Назначение | Права доступа | Тело запроса | Коды ответов | Примечания и валидации |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | `/api/auth/users/` | GET | Список пользователей Djoser | Авторизованный | Нет | 200, 401 | Служебный endpoint Djoser |
| 2 | `/api/auth/users/` | POST | Регистрация пользователя | Все | `username`, `password` | 201, 400 | Пароль проверяется валидаторами Django/Djoser |
| 3 | `/api/auth/users/me/` | GET, PATCH, PUT, DELETE | Текущий пользователь | Авторизованный | Поля пользователя | 200, 204, 400, 401 | Используется в Postman для проверки JWT |
| 4 | `/api/auth/users/{id}/` | GET, PATCH, PUT, DELETE | Пользователь по id | Авторизованный | Поля пользователя | 200, 204, 401, 404 | Служебный endpoint Djoser |
| 5 | `/api/auth/jwt/create/` | POST | Получение JWT | Все | `username`, `password` | 200, 401 | Возвращает `access` и `refresh` |
| 6 | `/api/auth/jwt/refresh/` | POST | Обновление JWT | Все | `refresh` | 200, 401 | Возвращает новый `access` |
| 7 | `/api/auth/jwt/verify/` | POST | Проверка JWT | Все | `token` | 200, 401 | Проверяет валидность токена |
| 8 | `/api/cats/` | GET | Список котов | Все | Нет | 200 | Поддерживает пагинацию |
| 9 | `/api/cats/` | POST | Создание кота | Авторизованный | `name`, `birth_year`, `breed`, `color`, `description`, `photo` | 201, 400, 401 | `owner` ставится автоматически, будущий `birth_year` запрещен |
| 10 | `/api/cats/{id}/` | GET | Детали кота | Все | Нет | 200, 404 |  |
| 11 | `/api/cats/{id}/` | PUT, PATCH, DELETE | Изменение или удаление кота | Владелец или админ | Поля кота | 200, 204, 400, 403, 404 | Чужой объект менять нельзя |
| 12 | `/api/categories/` | GET | Список категорий | Все | Нет | 200 |  |
| 13 | `/api/categories/` | POST | Создание категории | Админ | `name`, `slug`, `description` | 201, 400, 401, 403 | `name` и `slug` уникальны |
| 14 | `/api/categories/{id}/` | GET | Детали категории | Все | Нет | 200, 404 |  |
| 15 | `/api/categories/{id}/` | PUT, PATCH, DELETE | Управление категорией | Админ | Поля категории | 200, 204, 400, 401, 403, 404 |  |
| 16 | `/api/tags/` | GET | Список тегов | Все | Нет | 200 |  |
| 17 | `/api/tags/` | POST | Создание тега | Админ | `name`, `slug` | 201, 400, 401, 403 | `name` и `slug` уникальны |
| 18 | `/api/tags/{id}/` | GET | Детали тега | Все | Нет | 200, 404 |  |
| 19 | `/api/tags/{id}/` | PUT, PATCH, DELETE | Управление тегом | Админ | Поля тега | 200, 204, 400, 401, 403, 404 |  |
| 20 | `/api/posts/` | GET | Список записей | Все | Нет | 200 | Фильтры: `category`, `tags`, `cat`, `author`, `is_published`; поиск `search`; сортировка `ordering` |
| 21 | `/api/posts/` | POST | Создание записи | Авторизованный | `cat`, `title`, `text`, `category`, `tags`, `image`, `is_published` | 201, 400, 401 | Кот обязателен и должен принадлежать пользователю |
| 22 | `/api/posts/{id}/` | GET | Детали записи | Все | Нет | 200, 404 | Неопубликованные записи видит автор и админ |
| 23 | `/api/posts/{id}/` | PUT, PATCH, DELETE | Изменение или удаление записи | Автор или админ | Поля записи | 200, 204, 400, 403, 404 | `title` минимум 5 символов, `text` минимум 20 |
| 24 | `/api/posts/{post_id}/comments/` | GET | Комментарии записи | Все | Нет | 200, 404 | `post_id` берется из URL |
| 25 | `/api/posts/{post_id}/comments/` | POST | Создание комментария | Авторизованный | `text` | 201, 400, 401, 404 | Пустой текст запрещен |
| 26 | `/api/comments/{id}/` | GET | Детали комментария | Все | Нет | 200, 404 |  |
| 27 | `/api/comments/{id}/` | PUT, PATCH, DELETE | Изменение или удаление комментария | Автор или админ | `text` | 200, 204, 400, 403, 404 |  |
| 28 | `/api/schema/` | GET | OpenAPI schema | Все | Нет | 200 | drf-spectacular |
| 29 | `/api/docs/swagger/` | GET | Swagger UI | Все | Нет | 200 |  |
| 30 | `/api/docs/redoc/` | GET | Redoc | Все | Нет | 200 |  |
