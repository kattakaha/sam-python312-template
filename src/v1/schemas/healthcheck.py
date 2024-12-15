# First Party Library
from v1.schemas.common import BaseSchema


class HealthCheck(BaseSchema):
    """ヘルスチェックのレスポンススキーマ"""

    status: str
    version: str
