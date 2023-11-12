# syntax=docker/dockerfile:1
FROM python:3.12.0-alpine3.18
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
WORKDIR /app
RUN apk update && apk add gcc g++ libpq-dev python3-dev
COPY requirements.txt /app/
RUN pip install -r requirements.txt && pip install -r test_requirements
COPY . /app/
