FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY test_app.py .

EXPOSE 80

CMD ["gunicorn", "--bind", "0.0.0.0:80", "test_app:app"]