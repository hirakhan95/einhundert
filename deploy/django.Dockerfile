FROM python:3.10-slim-buster

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt .
RUN pip install --upgrade pip gunicorn && \
    pip install -r requirements.txt && \
    rm -rf /root/.cache/

COPY . .

EXPOSE 8000

RUN python manage.py makemigrations
RUN python manage.py migrate


CMD ["gunicorn", "--bind", ":8000", "--workers", "2", "einhundert_project.wsgi"]