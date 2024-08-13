# базовий образ
FROM python:3.12-alpine

LABEL maintainer="Backend Dev"

ENV PYTHONUNBUFFERED=1


# Встановлення необхідних системних залежностей
RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    postgresql-client \
    jpeg-dev \
    zlib-dev \
    libjpeg

# Оновлення pip та встановлення postgres адаптера для python
RUN pip install --upgrade pip && pip install psycopg2

# Копіювання проекту
COPY freelance_web_app/ /code/freelance_web_app/

# Встановлення залежностей з requirements.txt
RUN pip install -r /code/freelance_web_app/requirements.txt

# Встановлення робочого каталогу для виконання команд
WORKDIR /code/freelance_web_app

# Запуск сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]


