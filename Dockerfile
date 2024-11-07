FROM python:3.12-alpine AS base
ENV PYTHONUNBUFFERED=1 \
    PYTHONDONTWRITEBYTECODE=1 \
    PIP_NO_CACHE_DIR=off \
    PIP_DISABLE_PIP_VERSION_CHECK=on \
    PIP_DEFAULT_TIMEOUT=100 \
    POETRY_VERSION=1.8.3 \
    POETRY_HOME="/opt/poetry" \
    POETRY_VIRTUALENVS_CREATE=false \
    POETRY_NO_INTERACTION=1
ENV PATH="$POETRY_HOME/bin:$PATH"
RUN apk update && \
    apk add build-base \
    curl \
    postgresql-dev
RUN curl -sSL https://install.python-poetry.org | python3 -


FROM base AS api
WORKDIR /app
COPY poetry.lock pyproject.toml ./
RUN poetry install --with api

#FROM base AS worker
#WORKDIR /app
#COPY poetry.lock pyproject.toml ./
#RUN poetry install --with worker
