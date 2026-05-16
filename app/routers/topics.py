from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.orm import Session

from app.database import get_db
from app.models import Topic
from app.schemas import TopicOut

router = APIRouter()


@router.get("/topics", response_model=list[TopicOut])
def list_topics(db: Session = Depends(get_db)):
    stmt = select(Topic).order_by(Topic.topic_id)
    return db.execute(stmt).scalars().all()
