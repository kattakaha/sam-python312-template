# Standard Library
import os
from typing import Final

STAGE: Final[str] = os.environ.get("STAGE", "local")

API_VERSION: Final[str] = os.environ.get("API_VERSION", "latest")

API_CORS_ALLOED_ORIGINS: Final[str] = os.environ.get("API_CORS_ALLOWED_ORIGINS", "*")
