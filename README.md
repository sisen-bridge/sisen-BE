# sisen-BE

FastAPI backend serving read APIs for the Korea–Japan news service.

## Setup

Install dependencies and copy the env template:

```bash
pip install -r requirements.txt
cp .env.example .env
```

Set **one** of the two connection modes in `.env`:

- **Direct** — `DATABASE_URL=postgresql+pg8000://user:password@host:5432/dbname`
- **Cloud SQL Unix socket** — `INSTANCE_CONNECTION_NAME`, `DB_USER`, `DB_PASS`, `DB_NAME`
  (used on Cloud Run with the Cloud SQL Auth Proxy)

Apply migrations:

```bash
alembic upgrade head
```

## Run

```bash
uvicorn main:app --reload --port 8080
```

Docs at `http://localhost:8080/docs`.

## Endpoints

- `GET /topics` — list topics
- `GET /articles?topicId={id}` — list articles for a topic
- `GET /article?articleId={id}` — fetch article detail

## Docker

```bash
docker build -t sisen-be .
docker run --rm -p 8080:8080 --env-file .env sisen-be
```

## Deployment

`cloudbuild.yaml` deploys to Cloud Run with Cloud SQL over a Unix socket. Supply
the Cloud SQL env vars at deploy time.
