FROM python:3.10

WORKDIR /app

COPY . .

RUN pip install streamlit

EXPOSE 8501

CMD ["streamlit", "run", "main.py", "--server.address=0.0.0.0"]
