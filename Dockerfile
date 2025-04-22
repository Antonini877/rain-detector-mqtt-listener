FROM python:3.9-slim

WORKDIR /app

COPY /src /app
COPY requirements.txt /app
COPY .env /app
COPY config.yml /app


RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 1883

CMD ["python", "."]