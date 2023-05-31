# Bewise Task 1

## Docker Deploy

### 1. Create .env file with variables below:
```dotenv
SECRET_KEY="you-will-never-guess"
POSTGRES_USER=postgres
POSTGRES_PASSWORD=passwordpostgresql
POSTGRES_DB=bewise_db_1
POSTGRES_HOSTNAME=postgres
```
### 2. Deploy:
```shell
docker-compose up -d
```


## Development [![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/release/python-311/)

### 1. Install [PostgreSQL](https://www.postgresql.org/)

### 2. Install [Poetry](https://python-poetry.org)

### 3. Install dependencies:
```shell
poetry install --with dev
```
### 4. Create .env file with variables below:
```dotenv
SECRET_KEY=generate-random-symbols
POSTGRES_USER=paste-here-postgres-username
POSTGRES_PASSWORD=paste-here-postgres-password
POSTGRES_DB=bewise_db_1
POSTGRES_HOSTNAME=localhost
```
### 5. Change .flaskenv with variables below:
```dotenv
FLASK_ENV=development
FLASK_DEBUG=1
```
### 6. Migrations:
```shell
poetry run flask db upgrade
```
### 7. Run:
```shell
poetry run flask run
```

## Usage
### 1. Send the number of questions for the quiz:
```shell
curl --location 'http://127.0.0.1:5000/quizzes/' \
--header 'Content-Type: text/plain' \
--data '{
    "question_num": 1
}'
```
### Answer:
```json
{"category": 231, "answer": "Black Sea", "question": "Name of this sea is said to allude not to its dark water but its
storms", "local_uploaded_at": "2023-05-29T19:35:17.822564", "value": 300, "invalid_count": null, "game_id": 3067, "id":
3656, "updated_at": "2022-12-30T18:39:05.730000", "created_at": "2022-12-30T18:39:05.730000", "airdate":
"1985-11-19T20:00:00"}
```
