FROM python:3.12 AS builder 

WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


FROM python:3.12
WORKDIR /app
COPY --from=builder /usr/local /usr/local
COPY . .

ENV FLASK_APP=app.py
EXPOSE 8000

CMD ["python", "app.py"]

