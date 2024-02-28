import glob
from importlib import import_module

from fastapi import APIRouter, FastAPI


def setup_routes(app: FastAPI):
    base_router = APIRouter()
    app.include_router(base_router, prefix="/api")

    routes_files = glob.glob("**/src/main/routes/**routes.py", recursive=True)
    for file_path in routes_files:
        module_path = file_path.replace("/", ".").rstrip(".py")
        route_module = import_module(module_path)
        route_module.setup_routes(base_router)
