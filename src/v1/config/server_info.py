# Standard Library
from typing import Final, List

# Third Party Library
from aws_lambda_powertools.event_handler import CORSConfig
from aws_lambda_powertools.event_handler.openapi.models import Contact, HTTPBearer, SecurityScheme, Server
from pydantic.networks import AnyUrl

# First Party Library
from v1.config.settings import API_CORS_ALLOED_ORIGINS, STAGE

# APIのAuthor情報
API_AUTHOR_NAME: Final[str] = "Takahashi Katsuyuki"
API_AUTHOR_EMAIL: Final[str] = "kattakaha@gmail.com"
API_AUTHOR_URL: Final[AnyUrl] = AnyUrl("https://github.com/kattakaha")

# APIの共通のPrefix
API_COMMON_PREFIX: Final[str] = "v1"

# APIサーバーのAuthor情報
CONTACT: Final[Contact] = Contact(name=API_AUTHOR_NAME, email=API_AUTHOR_EMAIL, url=API_AUTHOR_URL)

# 各APIサーバーの説明
API_SERVER_DESCRIPTION: Final[dict[str, str]] = {
    "local": "Local Development Server",
    "dev": "Development Server",
    "stg": "Staging Server",
    "prod": "Production Server",
}

# APIのサーバー情報
SERVERS: Final[List[Server]] = [
    Server(
        url="/",
        description=API_SERVER_DESCRIPTION[STAGE],
        variables=None,
    )
]

# セキュリティー認証のヘッダー情報
AUTHORIZATION_HEADER: Final[dict[str, SecurityScheme]] = {"Authorization": HTTPBearer()}
SECURITY_REQUIREMENTS: Final[list[dict[str, List[str]]]] = [{"Authorization": []}]

# CORS 許可のオリジンリスト
API_CORS_ALLOWED_ORIGIN_LIST: Final[list[str]] = API_CORS_ALLOED_ORIGINS.split(",")

API_CORS_CONFIG = CORSConfig(
    allow_origin=API_CORS_ALLOWED_ORIGIN_LIST[0],
    extra_origins=API_CORS_ALLOWED_ORIGIN_LIST[1:],
    allow_credentials=False,
    max_age=600,
)
