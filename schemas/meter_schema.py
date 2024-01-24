from pydantic import BaseModel


class Meter(BaseModel):
    serial_number: int
    meter_type: str
    no_of_phase: int
    max_current: int
    owner_id: str
    owner_name: str
    cellphone: int
    municipal: str
    tarrif: str
    units: int
    other: str

    class Config:
        orm_mode = True


class CreateMeterResponse(BaseModel):
    id: int
    serial_number: int
    meter_type: str
    apikey: str
    no_of_phase: int
    max_current: int
    owner_id: str
    owner_name: str
    cellphone: int
    municipal: str
    tarrif: str
    units: int
    other: str
    created_at: str
    modified_at: str
