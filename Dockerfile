FROM python:3.12-slim

ENV PYTHONBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1
ENV SECRET_KEY=$SECRET_KEY

RUN mkdir /app
WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

CMD python manage.py collectstatic --noinput && python manage.py runserver 0.0.0.0:8000
