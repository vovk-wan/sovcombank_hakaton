import typing as t

from pydantic import BaseModel


class ExternalApiQuerySchema(BaseModel):
    function: str
    apikey: str
    symbol: str
    interval: str
    output_size: t.Optional[str] = None
