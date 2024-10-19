FROM python:3.11-slim

WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY api ./api

COPY app.py .

EXPOSE 5000

CMD ["python3", "-m", "flask", "--app", "app", "run", "--host=0.0.0.0"]
