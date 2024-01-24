from pydantic import BaseModel


class Config(BaseModel):
    configs: dict
    meter_id: int

    class Config:
        orm_mode = True
