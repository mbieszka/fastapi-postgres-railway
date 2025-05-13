# FastAPI + PostgreSQL on Railway

Minimal FastAPI app connected to PostgreSQL, deployable to Railway.

## Endpoints

- `/` – Hello World
- `/db` – Test connection to PostgreSQL

## Run locally

```bash
pip install -r requirements.txt
uvicorn main:app --reload
```