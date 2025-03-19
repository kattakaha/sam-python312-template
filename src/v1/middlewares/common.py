# Standard Library
from typing import Callable, TypeVar

# Third Party Library
from aws_lambda_powertools import Logger
from aws_lambda_powertools.event_handler import APIGatewayRestResolver, Response
from aws_lambda_powertools.event_handler.middlewares import NextMiddleware
from aws_lambda_powertools.middleware_factory import lambda_handler_decorator

logger = Logger()

T = TypeVar("T")


logger = Logger("Middleware")


def log_request_response(app: APIGatewayRestResolver, next_middleware: NextMiddleware) -> Response:
    """Middleware to log incoming request and response

    Args:
        app (APIGatewayRestResolver): app instance
        next_middleware (NextMiddleware): next middleware

    Returns:
        Response: api response
    """
    logger.info("Incoming request", path=app.current_event.path, request=app.current_event.raw_event)

    result = next_middleware(app)
    logger.info("Response received", response=result.__dict__)

    return result


# TODO: Authorization headerのチェックとデコード
@lambda_handler_decorator
def handler_middleware(handler: Callable[..., T], event: dict, context: dict) -> T:
    """アプリケーションのミドルウェア"""

    response = handler(event, context)

    return response
