# Third Party Library
from aws_lambda_powertools import Logger, Metrics, Tracer
from aws_lambda_powertools.event_handler import APIGatewayRestResolver
from aws_lambda_powertools.logging import correlation_paths
from aws_lambda_powertools.utilities.typing import LambdaContext

app = APIGatewayRestResolver()

app.enable_swagger(path="/swagger")


tracer = Tracer()
logger = Logger()
metrics = Metrics(namespace="Powertools")


@app.get("/healthcheck", operation_id="healthcheck")
@tracer.capture_method
def healthcheck():
    return {"status": "ok"}


@logger.inject_lambda_context(correlation_id_path=correlation_paths.API_GATEWAY_REST)
@tracer.capture_lambda_handler
def lambda_handler(event: dict, context: LambdaContext) -> dict:
    return app.resolve(event, context)
