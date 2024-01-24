from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from configs.database import SessionLocal
from cruds import meter_crud
from schemas.meter_schema import Meter

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
async def meter_root():
    return {"message": "welcome to routers"}


@router.get("/id/{id}")
async def get_single_meter(id: int, db: Session = Depends(get_db)):
    meter = meter_crud.get_meter(db, id)
    return meter


@router.get("/all")
async def get_all_meters(db: Session = Depends(get_db)):
    meter = meter_crud.get_meters(db)
    return meter


@router.post("/create")
async def create_meter(meter: Meter, db: Session = Depends(get_db)):
    meter = meter_crud.create_meter(db, meter)
    return meter


@router.patch("/update/{id}")
async def update_meter(id: int, body: dict, db: Session = Depends(get_db)):
    meter = meter_crud.update_meter(db, id, body)
    return meter


@router.delete("/delete/all")
async def delete_all_meters(db: Session = Depends(get_db)):
    rows = meter_crud.delete_all(db)
    return {"message": f"{str(rows)} rows have been deleted!"}


@router.delete("/delete/{id}")
async def delete_single_meter(id: int, db: Session = Depends(get_db)):
    meter = meter_crud.delete_meter(db, id)
    return meter
