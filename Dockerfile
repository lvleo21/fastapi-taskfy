FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD bash -c 'while !</dev/tcp/db/5432; do echo "Waiting for PostgreSQL..."; sleep 1; done; exec sh entrypoint.sh'
