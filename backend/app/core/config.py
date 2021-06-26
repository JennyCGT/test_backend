import secrets
from typing import Any, Dict, List, Optional, Union
import os
import sys
from dotenv import load_dotenv
from pydantic import AnyHttpUrl, BaseSettings, EmailStr, HttpUrl, PostgresDsn, validator
from starlette.config import Config
load_dotenv()

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8
    # SERVER_NAME: str
    # SERVER_HOST: AnyHttpUrl = "http:"
    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = os.getenv('BACKEND_CORS_ORIGINS')

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

    PROJECT_NAME: str = os.getenv('PROJECT_NAME')
    # SENTRY_DSN: Optional[HttpUrl] = None

    # @validator("SENTRY_DSN", pre=True)
    # def sentry_dsn_can_be_blank(cls, v: str) -> Optional[str]:
    #     if len(v) == 0:
    #         return None
    #     return v


    POSTGRES_USER = os.environ["RDS_USER"]
    POSTGRES_PASSWORD = os.environ["RDS_PASSWORD"]
    POSTGRES_SERVER = os.environ["RDS_HOST"]
    print(int(os.environ["RDS_PORT"]))
    POSTGRES_PORT = int(os.environ["RDS_PORT"])

    POSTGRES_DB = os.environ["RDS_DATABASE"]
    SQLALCHEMY_DATABASE_URI = f"postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}:{POSTGRES_PORT}/{POSTGRES_DB}"
    
    # SQLALCHEMY_DATABASE_URI: Optional[PostgresDsn] =PostgresDsn.build(
    #         scheme="postgresql",
    #         user=os.getenv("RDS_USER"),
    #         password=os.getenv("RDS_PASSWORD"),
    #         host=os.getenv("RDS_HOST"),
    #         path=f"/{os.getenv('RDS_DATABASE') or ''}",
    #     )


    # @validator("SQLALCHEMY_DATABASE_URI", pre=True)
    # def assemble_db_connection(cls, v: Optional[str], values: Dict[str, Any]) -> Any:
    #     return PostgresDsn.build(
    #         scheme="postgresql",
    #         user=os.getenv("POSTGRES_USER"),
    #         password=os.getenv("POSTGRES_PASSWORD"),
    #         host=os.getenv("POSTGRES_SERVER"),
    #         path=f"/{os.getenv('POSTGRES_DB') or ''}",
    #     )

    SMTP_TLS: bool = os.getenv('SMTP_TLS')
    SMTP_PORT: Optional[int] = os.getenv('SMTP_PORT')
    SMTP_HOST: Optional[str] = os.getenv('SMTP_HOST')
    SMTP_USER: Optional[str] = os.getenv('SMTP_USER')
    SMTP_PASSWORD: Optional[str] = os.getenv('SMTP_PASSWORD')
    # EMAILS_FROM_EMAIL: Optional[EmailStr] = "jrtec@info.io"
    EMAILS_FROM_NAME: Optional[str] = "JRTEC"


    EMAIL_RESET_TOKEN_EXPIRE_HOURS: int = 48
    EMAIL_TEMPLATES_DIR: str = "/app/app/email-templates/build"
    EMAILS_ENABLED: bool = False

    EMAIL_TEST_USER: EmailStr = "jenniferguayta@gmail.com"  # type: ignore
    FIRST_SUPERUSER: EmailStr = "jenniferguayta@gmail.com"
    FIRST_SUPERUSER_PASSWORD: str ="jenny123"
    USERS_OPEN_REGISTRATION: bool = False

    class Config:
        case_sensitive = True
        env_file = os.path.expanduser('~/.env')
print(Settings().dict())
settings = Settings()
