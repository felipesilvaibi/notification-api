import base64
import json
import random
import string
from typing import Callable

from fastapi import FastAPI, Request, Response
from starlette.middleware.base import BaseHTTPMiddleware

from main.config.logger import logger


class LoggingMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next: Callable) -> Response:
        request_id = request.headers.get("X-Request-ID", self._generate_random_id())

        request_params = await self._extract_request_parameters(request)

        with logger.contextualize(request_id=request_id):
            logger.info(f"Request {request.method}: {request.url.path}")
            logger.debug(f"Payload: {request_params}")

            try:
                response = await call_next(request)
            except Exception as e:  # pylint: disable=broad-except
                logger.error(e)
                raise e

            return response

    async def _extract_request_parameters(self, request: Request) -> str:
        if request.method == "GET":
            query_params = dict(request.query_params)

            path_params = request.path_params

            combined_params = {**query_params, **path_params}
            return json.dumps(combined_params)

        body_bytes = await request.body()
        body = body_bytes.decode()
        body = self.try_decode_topic_message(body)

        scope = request.scope
        scope["body"] = body_bytes
        request = Request(scope, receive=request._receive)  # pylint: disable=protected-access
        return body

    def _generate_random_id(self, length: int = 6) -> str:
        return "".join(random.choices(string.ascii_uppercase + string.digits, k=length))

    def try_decode_topic_message(self, request_body: str) -> str:
        try:
            if data := json.loads(request_body).get("message", {}).get("data"):
                return base64.b64decode(data).decode("utf-8")
        except json.decoder.JSONDecodeError:
            pass
        return request_body


def init_app(app: FastAPI):
    app.add_middleware(LoggingMiddleware)
    app.add_middleware(LoggingMiddleware)
