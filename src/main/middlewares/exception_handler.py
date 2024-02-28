from fastapi import Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel
from starlette.middleware.base import BaseHTTPMiddleware

from main.errors.invalid_param_error import InvalidParamError


def bad_request(error: Exception) -> JSONResponse:
    return JSONResponse(status_code=400, content={"error": str(error)})


def server_error() -> JSONResponse:
    return JSONResponse(status_code=500, content={"error": "Internal server error"})


def success(data: any) -> JSONResponse:
    return JSONResponse(status_code=200, content=data)


class ExceptionHandlerMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next) -> JSONResponse:
        try:
            response = await call_next(request)

            if isinstance(response, BaseModel):
                response = response.model_dump()

            return success(response)
        except InvalidParamError as ipe:
            return bad_request(ipe.errors)
        except Exception as error:
            print(error)
            return server_error()
