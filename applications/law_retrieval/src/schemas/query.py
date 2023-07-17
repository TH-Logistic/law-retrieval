from pydantic import BaseModel, Field


class Query(BaseModel):
    query: str = Field(min_length=1)


class QueryOut(BaseModel):
    type: str
    code: str | None = None
    title: str | None = None
    content: str | None = None
