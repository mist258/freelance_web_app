# базовий образ
FROM python:3.12-alpine

ENV PYTHONUNBUFFERED=1

WORKDIR /code

COPY requirements.txt /code/

COPY . /code/


RUN pip install --no-cache-dir -r requirements.txt

RUN apk update && apk add --no-cache \
    gcc \
    musl-dev \
    postgresql-dev \
    postgresql-client
#    jpeg-dev \
#    zlib-dev \
#    libjpeg
RUN pip install --upgrade pip && pip install psycopg2


