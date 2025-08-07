# Используем базовый образ Python
FROM python:3.12-slim

# Устанавливаем рабочую директорию
WORKDIR /app

# Устанавливаем Poetry
ENV POETRY_HOME="/opt/poetry"
ENV POETRY_VIRTUALENVS_IN_PROJECT=true
ENV PATH="$POETRY_HOME/bin:$PATH"

RUN pip install poetry && poetry self update


# Копируем файлы проекта, необходимые для установки зависимостей
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN poetry install --no-root --without dev

# Копируем исходный код приложения
COPY src/ ./src/

COPY tests/ ./tests/

# Добавляем наш код в PYTHONPATH
ENV PYTHONPATH=/app/src


# Команда для запуска приложения
CMD ["poetry", "run", "python", "src/main.py"]