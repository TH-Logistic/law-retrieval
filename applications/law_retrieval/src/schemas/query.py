from pydantic import BaseModel, Field
from typing import Optional


class Query(BaseModel):
    query: str = Field(min_length=1)


class QueryOut(BaseModel):
    type: str
    code: Optional[str] = None
    title: Optional[str] = None
    content: Optional[str] = None

    class Config:
        arbitrary_types_allowed = True
