# Einhundert Case Study

## Build and Start project with django

### 1. Require Migrations 
```bash
python manage.py makemigrations
python manage.py migrate
```
It will create sqlite database and create required tables

### 2. Run Server
```bash
python manage.py runserver
```

## Build and Start server on docker

- PreRequisite: [Docker](https://docs.docker.com/engine/install/) 
- Tested on: Docker version 23.0.5, build bc4487a

### Build

```bash
docker compose build
```

### Start docker container

```bash
docker compose up
```

or in background

```bash
docker compose up -d
```

### Shutdown docker containers

```bash
docker compose down
```

## Postman

Postman folder is provided in this repository.

### Steps to Use the API via Postman:

1. Open Postman and import the collection from the project's `postman` folder into your Postman workspace.
2. The imported collection includes the API endpoint and sample parameters used for testing.
3. Send a GET request to the endpoint with the required JSON payload.





