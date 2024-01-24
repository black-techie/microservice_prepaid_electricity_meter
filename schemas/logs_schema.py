from pydantic import BaseModel


class Log(BaseModel):
    voltage: float
    power: float
    units: float
    alerts: list
    params: list
    response: list
    api_key: str

    class Config:
        orm_mode = True
