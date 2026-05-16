from fastapi import APIRouter, Depends, HTTPException, Query
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Article
from app.schemas import ArticleDetail, ArticleListItem

router = APIRouter()


@router.get("/articles", response_model=list[ArticleListItem])
def list_articles(
    topicId: int = Query(..., description="Filter articles by topic id"),
    db: Session = Depends(get_db),
):
    stmt = (
        select(Article)
        .where(Article.topic_id == topicId)
        .order_by(Article.article_id)
    )
    return db.execute(stmt).scalars().all()


@router.get("/article", response_model=ArticleDetail)
def article_detail(
    articleId: int = Query(..., description="Article id"),
    db: Session = Depends(get_db),
):
    article = db.get(Article, articleId)
    if article is None:
        raise HTTPException(status_code=404, detail="Article not found")
    return article
