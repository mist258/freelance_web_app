# базовий образ
FROM python:3.12-alpine

LABEL maintainer="Backend Dev"

ENV PYTHONUNBUFFERED=1

#WORKDIR /code
#COPY . /code/

RUN apk update

# залежності до з'єднання з бд
RUN apk add --no-cache gcc musl-dev postgresql-dev postgresql-client

# postgres адаптер для python
RUN pip install psycopg2

# for pillow

RUN apk add --no-cache jpeg-dev zlib-dev libjpeg

#RUN mkdir /code

RUN pip install --upgrade pip

COPY freelance_web_app/requirements.txt /tmp

RUN cd /tmp && pip install -r requirements.txt
