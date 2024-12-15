# Standard Library
from http import HTTPStatus

# Third Party Library
from aws_lambda_powertools.event_handler.openapi.types import OpenAPIResponse
from pydantic import BaseModel, Field


class BadRequestErrorSchema(BaseModel):
    """Bad Request Error Schema"""

    status_code: int = Field(
        ...,
        title="HTTPステータスコード",
        description="""
HTTPのステータスコードです。
詳しくは、[HTTPステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Status)を参照してください。
これがレスポンスの型に入るのはLambda Powertoolsの仕様です。
    """,
        examples=[HTTPStatus.BAD_REQUEST.value],
    )
    message: str = Field(
        ...,
        title="エラーメッセージ",
        description="Bad Request Error Message",
        examples=["Bad Request"],
    )


class UnauthorizedErrorSchema(BaseModel):
    """Unauthorized Error Schema"""

    status_code: int = Field(
        ...,
        title="HTTPステータスコード",
        description="""
HTTPのステータスコードです。
詳しくは、[HTTPステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Status)を参照してください。
これがレスポンスの型に入るのはLambda Powertoolsの仕様です。
    """,
        examples=[HTTPStatus.UNAUTHORIZED.value],
    )
    message: str = Field(
        ...,
        title="エラーメッセージ",
        description="Unauthorized Error Message",
        examples=["Unauthorized"],
    )


class NotFoundErrorSchema(BaseModel):
    """Not Found Error Schema"""

    status_code: int = Field(
        ...,
        title="HTTPステータスコード",
        description="""
HTTPのステータスコードです。
詳しくは、[HTTPステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Status)を参照してください。
これがレスポンスの型に入るのはLambda Powertoolsの仕様です。
""",
        examples=[HTTPStatus.NOT_FOUND.value],
    )
    message: str = Field(
        ...,
        title="エラーメッセージ",
        description="Not Found Error Message",
        examples=["Not Found"],
    )


class InternalServerErrorSchema(BaseModel):
    """Internal Server Error Schema"""

    status_code: int = Field(
        ...,
        title="HTTPステータスコード",
        description="""
HTTPのステータスコードです。
詳しくは、[HTTPステータスコード](https://developer.mozilla.org/ja/docs/Web/HTTP/Status)を参照してください。
これがレスポンスの型に入るのはLambda Powertoolsの仕様です。
""",
        examples=[HTTPStatus.INTERNAL_SERVER_ERROR.value],
    )
    message: str = Field(
        ...,
        title="エラーメッセージ",
        description="Internal Server Error Message",
        examples=["Internal Server Error"],
    )


BAD_REQUEST_ERROR = OpenAPIResponse(
    description="Bad Request",
    content={"application/json": {"schema": BadRequestErrorSchema.model_json_schema()}},
)
UNAUTHORIZED_ERROR = OpenAPIResponse(
    description="Unauthorized Error",
    content={"application/json": {"schema": UnauthorizedErrorSchema.model_json_schema()}},
)
NOT_FOUND_ERROR = OpenAPIResponse(
    description="Not Found Error",
    content={"application/json": {"schema": NotFoundErrorSchema.model_json_schema()}},
)
INTERNAL_SERVER_ERROR = OpenAPIResponse(
    description="Internal Server Error",
    content={"application/json": {"schema": InternalServerErrorSchema.model_json_schema()}},
)
