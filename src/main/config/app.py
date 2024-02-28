from fastapi import FastAPI

from main.config.middlewares import setup_middlewares
from main.config.routes import setup_routes

app = FastAPI(openapi_url="/docs")

setup_middlewares(app)
setup_routes(app)
