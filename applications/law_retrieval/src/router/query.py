from fastapi import APIRouter, Path, Depends, Body
from ..schemas.query import Query, QueryOut
from src.crud.query import QueryService

router = APIRouter(prefix="")

query_service = QueryService()


@router.post("/query")
def query_article(body: Query):
    return query_service.query_articles(body.query)
