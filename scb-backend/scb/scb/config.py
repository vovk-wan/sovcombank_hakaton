from pydantic import BaseSettings


class Config(BaseSettings):
    debug: bool = True
    secret_key: str = (
        "0000000000000000000000000000000000000000000000000000000000000000001"
    )
    allowed_hosts: str = "127.0.0.1 0.0.0.0"
    csrf_trusted_origins: str = (
        "http://0.0.0.0 http://127.0.0.1 http://0.0.0.0:8887 http://127.0.0.1:8887"
    )
    django_db_engine: str = "django.db.backends.postgresql"
    django_db_host: str = "127.0.0.1"
    django_db_port: str = "5732"
    django_db_name: str = "postgres"
    django_db_user: str = "postgres"
    django_db_password: str = "PostgresPassword"
    rabbit_host: str
    rabbit_port: int
    rabbit_user: str
    rabbit_password: str
    redis_host: str
    redis_port: int
    redis_db: int = 0
    celery_count: int = 2
