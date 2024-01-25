ARG PYTHON_VERSION=3.12
FROM python:${PYTHON_VERSION}-alpine3.19
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1 \
    POETRY_VIRTUALENVS_CREATE=false
WORKDIR /app
COPY poetry.lock pyproject.toml /app/
RUN apk update && apk add bash curl build-base libffi-dev libpq-dev python3-dev
RUN curl -sSL https://install.python-poetry.org | python3 - --preview
RUN poetry install
COPY . /app/
