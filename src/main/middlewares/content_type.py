from fastapi import Request
from starlette.middleware.base import BaseHTTPMiddleware


class ContentTypeMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        response = await call_next(request)

        response.headers["Content-Type"] = "application/json"

        return response
