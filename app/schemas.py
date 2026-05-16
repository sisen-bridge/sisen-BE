from pydantic import BaseModel, ConfigDict


class TopicOut(BaseModel):
    topic_id: int
    name: str
    ko_neutral_title: str | None
    ja_neutral_title: str | None
    ko_summary: str | None
    ja_summary: str | None

    model_config = ConfigDict(from_attributes=True)


class ArticleListItem(BaseModel):
    """Lightweight payload used by GET /articles?topicId=..."""
    article_id: int
    press_name: str
    nation: str | None
    ko_title: str | None
    ja_title: str | None

    model_config = ConfigDict(from_attributes=True)


class ArticleDetail(BaseModel):
    """Full payload used by GET /article?articleId=..."""
    article_id: int
    press_name: str
    nation: str | None
    ko_title: str | None
    ja_title: str | None
    url: str | None
    ko_text: str | None
    ja_text: str | None

    model_config = ConfigDict(from_attributes=True)
