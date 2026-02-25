FROM python:3.13-slim

WORKDIR /app

RUN pip install --no-cache-dir psycopg[binary]

COPY entrypoint.py /app/entrypoint.py

ENTRYPOINT ["python", "/app/entrypoint.py"]