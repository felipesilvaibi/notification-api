from fastapi import Request
from fastapi.responses import JSONResponse
from starlette.middleware.base import BaseHTTPMiddleware

from presentation.errors.generic_errors import (GenericClientError,
                                                GenericServerError)


def bad_request(error: str, status_code: int = 400) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": error})


def server_error(error: Exception, status_code: int = 500) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": error})


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> JSONResponse:
        try:
            return await call_next(request)
        except GenericClientError as gen_client_error:
            return bad_request(gen_client_error.args[0])
        except GenericServerError as gen_server_error:
            return server_error(gen_server_error.args[0])
        except Exception:
            return server_error("Internal server error")
