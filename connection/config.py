from typing import Optional

from dotenv import load_dotenv
from pydantic_settings import BaseSettings

load_dotenv()

class Settings(BaseSettings):
    MONGO_USER: str
    MONGO_PASS: Optional[str]
    MONGODB_NAME: str
    MONGO_DOMAIN: str

    uri: str

    POSTGRES_ENGINE: str
    POSTGRES_NAME: str
    POSTGRES_USER: str
    POSTGRES_PASSWORD: Optional[str]
    POSTGRES_HOST: str
    POSTGRES_PORT: int = 5432

    EMAIL_BACKEND: str = 'django.core.mail.backends.smtp.EmailBackend'
    EMAIL_HOST: str = 'smtp.meta.ua'
    EMAIL_PORT: int = 465
    EMAIL_STARTTLS: bool = False
    EMAIL_USE_SSL: bool = True
    EMAIL_USE_TLS: bool = False
    EMAIL_HOST_USER: str = 'example@meta.ua'
    EMAIL_HOST_PASSWORD: Optional[str]
    DEFAULT_FROM_EMAIL: str

    DJANGO_SECRET_KEY: str

    class Config:
        env_file = "python_web_10_v2/.env"
        env_file_encoding = "utf-8"

config = Settings()
