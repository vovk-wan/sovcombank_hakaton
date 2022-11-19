import typing as t

from pydantic import BaseModel


class ExternalApiQuerySchema(BaseModel):
    function: str
    apikey: str
    symbol: str
    interval: str
    output_size: t.Optional[str] = None


class RegistrationInSchema(BaseModel):
    login: str
    password: str


class SuccessRegistrationSchema(BaseModel):
    """
    Ответ об усперной регистрации
    """

    status: str
    login: str


class RegistrationResponseSchema(BaseModel):
    """
    Схема ответа об успешной регистрации
    """

    data: SuccessRegistrationSchema
