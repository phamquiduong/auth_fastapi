# FastAPI-Auth
### Server
- Python 3.13
- FastAPI

### Migrations
- SQLite3
- Alembic

<br>

## Python enviroment
#### Install Migrations Libs
```bash
pip install -r .\requirements-migration.txt
```

#### Install FastAPI Libs
```bash
pip install -r .\requirements.txt
```

<br>

## Alembic Migrations
#### Create a Migration Script
```bash
alembic revision -m "create account table"
```

#### Running our First Migration
```bash
alembic upgrade head
```

<br>

## FastAPI Server
#### Start server
```bash
uvicorn main:app --host 127.0.0.1 --port 8000 --reload
```
