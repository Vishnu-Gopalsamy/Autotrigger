FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip install Flask

EXPOSE 8501

CMD ["python", "main.py"]
