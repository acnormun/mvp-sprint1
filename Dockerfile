FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir flask flask_sqlalchemy flask-cors flasgger requests

EXPOSE 5000

CMD ["python", "app.py"]
