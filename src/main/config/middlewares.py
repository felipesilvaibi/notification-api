from fastapi import FastAPI

from main.middlewares.cors import CORSMiddleware
from main.middlewares.exception import ExceptionMiddleware
from main.middlewares.logging import LoggingMiddleware


def setup_middlewares(app: FastAPI):
    app.add_middleware(CORSMiddleware)
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(ExceptionMiddleware)
