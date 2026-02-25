FROM python:3.13-slim

WORKDIR /app

COPY app /app/app

ENTRYPOINT ["python", "-m", "app.main"]