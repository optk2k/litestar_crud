FROM python:3.12-slim-bookworm

WORKDIR /app

COPY . /app

RUN cd src && pip install --no-cache-dir poetry && poetry install --no-root --without dev

EXPOSE 8080

ENTRYPOINT cd src && poetry run granian --interface asgi --host 0.0.0.0 --port 8080 app:app

