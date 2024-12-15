# Standard Library
from http import HTTPStatus

# Third Party Library
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

# First Party Library
from v1.config.server_info import API_CORS_CONFIG, CONTACT, SERVERS
from v1.config.settings import API_VERSION, STAGE
from v1.schemas import errors
from v1.schemas.healthcheck import HealthCheck

SERVICE_NAME = "AppApiHandler"

is_debug = True if STAGE == "local" or STAGE == "dev" else False

app = APIGatewayRestResolver(cors=API_CORS_CONFIG, enable_validation=True, debug=is_debug)

if STAGE == "local" or STAGE == "dev":
    app.enable_swagger(
        path="/swagger",
        title="SAM Python3.12 template API 仕様書",
        summary="SAM Python3.12 template API Specification",
        description="""
## 概要

SAM Python3.12 template API API仕様書。

## 仕様書について

仕様書（ドキュメント）の生成は、AWS Lambda Powertools の OpenAPI version 3.1.0 仕様書を使用し、半自動で生成されています。
もし、APIについての質問や提案があれば、髙橋までご連絡ください。

## リクエストとレスポンスのフォーマット

リクエストとレスポンスのフォーマットは、JSON 形式で提供されます。
リクエストに関しての詳細は、各エンドポイントの仕様を参照してください。

## APIのバージョン情報

APIのバージョンはローカルからデプロイされた場合`latest` になります。
GitHub Actions によるCI/CD でデプロイされた場合は、コミットハッシュが付与されたバージョンになります。このバージョン情報は、ヘルスチェックエンドポイントで確認することもできます。
""",
        contact=CONTACT,
        servers=SERVERS,
    )


tracer = Tracer(SERVICE_NAME)
logger = Logger(SERVICE_NAME)
metrics = Metrics(namespace=SERVICE_NAME)


@app.get(
    "/healthcheck",
    cors=False,
    summary="Health Check",
    description="""
## 概要

サーバーの稼働状況を確認するためのエンドポイントです。

## 詳細

基本的には常に Status Code 200: で`ok` が返却されます。
それ以外の場合は、サーバーに問題が発生している可能性がありますのでお手数ですが、髙橋までご連絡ください。

## APIのバージョン情報

APIのバージョンは、環境変数で`API_VERSION_HASH` として注入されます。ローカルからデプロイされた場合`latest` になります。

## 変更履歴

- 2024/12/13: ヘルスチェックエンドポイントを追加
""",
    operation_id="healthcheck",
    responses={
        HTTPStatus.OK: {"description": "Health Check Status"},
        HTTPStatus.BAD_REQUEST: errors.BAD_REQUEST_ERROR,
        HTTPStatus.UNAUTHORIZED: errors.UNAUTHORIZED_ERROR,
        HTTPStatus.NOT_FOUND: errors.NOT_FOUND_ERROR,
        HTTPStatus.INTERNAL_SERVER_ERROR: errors.INTERNAL_SERVER_ERROR,
    },
)
@tracer.capture_method
def healthcheck() -> HealthCheck:
    return HealthCheck(status="ok", version=API_VERSION)


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
