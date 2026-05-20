# Postman Requests

Коллекция находится в `docs/postman/kittygram_blog.postman_collection.json`. Запросы рассчитаны на последовательный запуск: сначала создается основной пользователь, затем администраторский токен, кот, категория, тег, запись, комментарий и негативные проверки прав доступа.

Перед запуском проверь переменные коллекции:

| Переменная | Значение по умолчанию | Назначение |
| --- | --- | --- |
| `base_url` | `http://localhost` | адрес API через nginx |
| `username` | `arseniy` | основной пользователь |
| `password` | `StrongPass123` | пароль основного пользователя |
| `second_username` | `ivan` | второй пользователь для проверки 403 |
| `second_password` | `StrongPass123` | пароль второго пользователя |
| `admin_username` | `admin` | суперпользователь |
| `admin_password` | `AdminPass123` | пароль суперпользователя |
| `access_token`, `refresh_token` | пусто | заполняются после JWT-запроса |
| `admin_access_token` | пусто | заполняется после JWT-запроса администратора |
| `second_access_token` | пусто | заполняется после JWT-запроса второго пользователя |
| `cat_id`, `post_id`, `comment_id`, `category_id`, `tag_id` | пусто | заполняются после создания объектов |

| № | Запрос | Метод | URL | Headers | Body | Ожидаемый код | Смысл проверки |
| --- | --- | --- | --- | --- | --- | --- | --- |
| 1 | Register User | POST | `{{base_url}}/api/auth/users/` | `Content-Type` | `username`, `password` | 201 | Регистрация основного пользователя |
| 2 | Create JWT Token | POST | `{{base_url}}/api/auth/jwt/create/` | `Content-Type` | `username`, `password` | 200 | Получение `access_token` и `refresh_token` |
| 3 | Refresh JWT Token | POST | `{{base_url}}/api/auth/jwt/refresh/` | `Content-Type` | `refresh` | 200 | Обновление access-токена |
| 4 | Verify JWT Token | POST | `{{base_url}}/api/auth/jwt/verify/` | `Content-Type` | `token` | 200 | Проверка JWT |
| 5 | Get Current User | GET | `{{base_url}}/api/auth/users/me/` | `Authorization: Bearer {{access_token}}` | Нет | 200 | Проверка авторизации |
| 6 | Create Admin JWT Token | POST | `{{base_url}}/api/auth/jwt/create/` | `Content-Type` | `admin_username`, `admin_password` | 200 | Получение токена администратора |
| 7 | Create Cat | POST | `{{base_url}}/api/cats/` | `Authorization: Bearer {{access_token}}` | `name`, `birth_year`, `breed`, `color` | 201 | Кот создается обычным пользователем |
| 8 | List Cats | GET | `{{base_url}}/api/cats/` | Нет | Нет | 200 | Публичный список котов |
| 9 | Get Cat Detail | GET | `{{base_url}}/api/cats/{{cat_id}}/` | Нет | Нет | 200 | Детали кота |
| 10 | Patch Own Cat | PATCH | `{{base_url}}/api/cats/{{cat_id}}/` | `Authorization: Bearer {{access_token}}` | `color` | 200 | Владелец редактирует своего кота |
| 11 | Create Category | POST | `{{base_url}}/api/categories/` | `Authorization: Bearer {{admin_access_token}}` | `name`, `slug`, `description` | 201 | Категорию создает администратор |
| 12 | List Categories | GET | `{{base_url}}/api/categories/` | Нет | Нет | 200 | Публичный список категорий |
| 13 | Create Tag | POST | `{{base_url}}/api/tags/` | `Authorization: Bearer {{admin_access_token}}` | `name`, `slug` | 201 | Тег создает администратор |
| 14 | List Tags | GET | `{{base_url}}/api/tags/` | Нет | Нет | 200 | Публичный список тегов |
| 15 | Create Blog Post | POST | `{{base_url}}/api/posts/` | `Authorization: Bearer {{access_token}}` | `cat`, `title`, `text`, `category`, `tags` | 201 | Запись создается для своего кота |
| 16 | List Blog Posts | GET | `{{base_url}}/api/posts/` | Нет | Нет | 200 | Публичный список записей |
| 17 | Get Blog Post Detail | GET | `{{base_url}}/api/posts/{{post_id}}/` | Нет | Нет | 200 | Детали записи |
| 18 | Search Blog Posts | GET | `{{base_url}}/api/posts/?search=Мурка` | Нет | Нет | 200 | Поиск по записи, коту и автору |
| 19 | Filter Blog Posts By Category | GET | `{{base_url}}/api/posts/?category=...` | Нет | Нет | 200 | Фильтр по slug категории |
| 20 | Filter Blog Posts By Tag | GET | `{{base_url}}/api/posts/?tags=...` | Нет | Нет | 200 | Фильтр по slug тега |
| 21 | Filter Blog Posts By Cat | GET | `{{base_url}}/api/posts/?cat={{cat_id}}` | Нет | Нет | 200 | Фильтр по id кота |
| 22 | Create Comment | POST | `{{base_url}}/api/posts/{{post_id}}/comments/` | `Authorization: Bearer {{access_token}}` | `text` | 201 | Создание комментария к записи |
| 23 | List Post Comments | GET | `{{base_url}}/api/posts/{{post_id}}/comments/` | Нет | Нет | 200 | Публичный список комментариев записи |
| 24 | Patch Own Comment | PATCH | `{{base_url}}/api/comments/{{comment_id}}/` | `Authorization: Bearer {{access_token}}` | `text` | 200 | Автор редактирует свой комментарий |
| 25 | Register Second User | POST | `{{base_url}}/api/auth/users/` | `Content-Type` | `second_username`, `second_password` | 201 | Второй пользователь для негативного сценария |
| 26 | Create Second User JWT Token | POST | `{{base_url}}/api/auth/jwt/create/` | `Content-Type` | `second_username`, `second_password` | 200 | Получение `second_access_token` |
| 27 | Forbidden Update Another User Post | PATCH | `{{base_url}}/api/posts/{{post_id}}/` | `Authorization: Bearer {{second_access_token}}` | `title` | 403 | Второй пользователь не может менять чужую запись |
| 28 | Validation Error Create Post Without Cat | POST | `{{base_url}}/api/posts/` | `Authorization: Bearer {{access_token}}` | `title`, `text` | 400 | Нельзя создать запись без кота |
| 29 | Validation Error Create Post With Short Title | POST | `{{base_url}}/api/posts/` | `Authorization: Bearer {{access_token}}` | короткий `title` | 400 | Заголовок короче 5 символов запрещен |
| 30 | Validation Error Empty Comment | POST | `{{base_url}}/api/posts/{{post_id}}/comments/` | `Authorization: Bearer {{access_token}}` | пустой `text` | 400 | Пустой комментарий запрещен |
| 31 | Get OpenAPI Schema | GET | `{{base_url}}/api/schema/` | Нет | Нет | 200 | Проверка OpenAPI-схемы |
| 32 | Get Swagger UI | GET | `{{base_url}}/api/docs/swagger/` | Нет | Нет | 200 | Проверка Swagger UI |
| 33 | Get Redoc | GET | `{{base_url}}/api/docs/redoc/` | Нет | Нет | 200 | Проверка Redoc |
