from datetime import datetime

from sqlalchemy import DateTime, ForeignKey, Index, String, Text, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.database import Base


class Topic(Base):
    __tablename__ = "topic"

    topic_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(255))
    ko_summary: Mapped[str | None] = mapped_column(Text)
    ja_summary: Mapped[str | None] = mapped_column(Text)
    ko_neutral_title: Mapped[str | None] = mapped_column(String(512))
    ja_neutral_title: Mapped[str | None] = mapped_column(String(512))
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    articles: Mapped[list["Article"]] = relationship(back_populates="topic")


class Article(Base):
    __tablename__ = "article"

    article_id: Mapped[int] = mapped_column(primary_key=True)
    topic_id: Mapped[int] = mapped_column(ForeignKey("topic.topic_id"))
    press_name: Mapped[str] = mapped_column(String(255))
    nation: Mapped[str | None] = mapped_column(String(255))
    url: Mapped[str | None] = mapped_column(String(2048))
    ko_title: Mapped[str | None] = mapped_column(String(512))
    ja_title: Mapped[str | None] = mapped_column(String(512))
    ko_text: Mapped[str | None] = mapped_column(Text)
    ja_text: Mapped[str | None] = mapped_column(Text)
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True), server_default=func.now()
    )

    topic: Mapped["Topic"] = relationship(back_populates="articles")

    __table_args__ = (Index("idx_article_topic_id", "topic_id"),)
