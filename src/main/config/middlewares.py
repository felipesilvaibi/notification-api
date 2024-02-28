from fastapi import FastAPI

from main.middlewares.content_type import ContentTypeMiddleware
from main.middlewares.cors import CORSMiddleware
from main.middlewares.exception_handler import ExceptionHandlerMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(CORSMiddleware)
    app.add_middleware(ContentTypeMiddleware)
    app.add_middleware(ExceptionHandlerMiddleware)
