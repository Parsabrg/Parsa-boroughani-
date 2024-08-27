FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir flask psutil

EXPOSE 5000

CMD ["python", "main.py"]

