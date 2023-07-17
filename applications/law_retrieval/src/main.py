from fastapi import FastAPI, Request, HTTPException
from pymongo import errors
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from src.models.base_response import BaseResponse
from fastapi.middleware.cors import CORSMiddleware
from src.router import query
from src.crud.query import QueryService

app = FastAPI()

app.include_router(router=query.router)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.exception_handler(HTTPException)
def handle_http_exception(req: Request, err: HTTPException):
    response = BaseResponse()
    response.message = err.detail
    response.success = False
    response.data = None

    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=err.status_code
    )


@app.exception_handler(Exception)
def handle_exceptions(req: Request, err: Exception):
    message = ''
    status_code = 500
    if isinstance(err, HTTPException):
        message = err.detail
        status_code = err.status_code

    if isinstance(err, errors.DuplicateKeyError):
        message = err.details['errmsg']
        status_code = 400

    response = BaseResponse()
    response.message = message

    return JSONResponse(
        content=jsonable_encoder(response),
        status_code=status_code
    )


@app.on_event("startup")
async def startup_event():
    pass
