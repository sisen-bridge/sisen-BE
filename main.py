from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers import articles, topics

app = FastAPI(title="sisen-BE")

# Allow any origin during development; tighten this for production.
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

app.include_router(topics.router)
app.include_router(articles.router)


@app.get("/")
def root():
    return {"status": "ok"}
