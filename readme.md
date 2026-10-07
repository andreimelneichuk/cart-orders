# cart-orders

Учебный REST API на FastAPI для товаров и заказов с проверкой остатков на складе.

## Стек

- Python, FastAPI
- SQLAlchemy (async) + asyncpg
- PostgreSQL
- pytest
- Docker, docker-compose

## Модели

- `Product`: название, описание, цена, остаток (`stock`).
- `Order`: дата создания, статус (`in_progress`, `shipped`, `delivered`).
- `OrderItem`: позиция заказа (товар и количество).

## Эндпоинты

| Метод | Путь | Описание |
| :--- | :--- | :--- |
| POST | `/products/` | Создать товар |
| GET | `/products/{product_id}` | Получить товар по id |
| POST | `/orders/` | Создать заказ. Остаток товара уменьшается; если товара не хватает, возвращается 400 |

Swagger UI доступен по адресу `http://localhost:8000/docs`.

## Запуск

```bash
git clone https://github.com/andreimelneichuk/cart-orders.git
cd cart-orders
docker-compose up --build
```

Строка подключения к БД задана в `app/database.py` и рассчитана на сервис `db` из `docker-compose.yml`.

## Тесты

```bash
pytest
```

## Ограничения

- Миграций нет, таблицы автоматически не создаются: их нужно создать вручную (например, через `Base.metadata.create_all`).
- `crud.create_order` обращается к `order_data.status`, но в схеме `OrderCreate` этого поля нет.
- Есть один тест (`test_create_product`).
