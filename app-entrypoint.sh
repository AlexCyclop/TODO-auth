#!/bin/sh
set -e

echo "Применение миграций Alembic..."
alembic upgrade head

echo "Запуск Uvicorn..."
exec uvicorn src.main:app --host 0.0.0.0 --port 8080 --reload
