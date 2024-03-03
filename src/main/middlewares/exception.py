from fastapi import Request
from fastapi.responses import JSONResponse
from loguru import logger
from starlette.middleware.base import BaseHTTPMiddleware

from src.presentation.errors.generic_errors import (
    GenericClientError,
    GenericServerError,
)


def bad_request(error: str, status_code: int = 400) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": error})


def server_error(error: str, status_code: int = 500) -> JSONResponse:
    return JSONResponse(status_code=status_code, content={"error": error})


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> JSONResponse:
        try:
            return await call_next(request)
        except GenericClientError as gen_client_error:
            error = gen_client_error.args[0]
            logger.warning(error)
            return bad_request(error)
        except GenericServerError as gen_server_error:
            error = gen_server_error.args[0]
            logger.error(gen_server_error.args[0])
            return server_error(gen_server_error.args[0])
        except Exception as e:
            logger.error(e)
            return server_error("Internal server error")
