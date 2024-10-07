# базовий образ
FROM python:3.12-alpine
MAINTAINER Python dev

ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=OFF \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.2 \
    POETRY_NO_INTERACTION=1 \
    COLUMNS=80

RUN apk update
RUN apk add --no-cache  \
    gcc  \
    musl-dev  \
    postgresql-dev \
    postgresql-client \
    curl \
    jpeg-dev \
    zlib-dev \
    libjpeg

RUN mkdir /web
WORKDIR /web

ENV POETRY_HOME=/usr/local/poetry
RUN  curl -sSL https://install.python-poetry.org | python3 -
ENV PATH=$POETRY_HOME/bin:$PATH

COPY pyproject.toml /web/

RUN poetry config virtualenvs.create false
RUN poetry lock
RUN poetry install


