from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi import APIRouter
from configs.database import SessionLocal
from cruds import logs_crud
from schemas.logs_schema import Log
router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
async def log_root():
    return {"message": "welcome to the index of the logger"}


@router.get("/id/{id}")
async def get_single_log(id: int, db: Session = Depends(get_db)):
    logs = logs_crud.get_log(db, id)
    return logs


@router.get("/all")
async def get_all_logs(db: Session = Depends(get_db)):
    logs = logs_crud.get_logs(db)
    return logs


@router.post("/create")
async def create_log(log: Log, db: Session = Depends(get_db)):
    logs = logs_crud.create_log(db, log)
    return logs


# @router.patch("/update/{id}")
# async def update_log():
#     return {"message": "Meter logs will be updated here"}
#
#
# @router.delete("/delete")
# async def delete_all_logs():
#     return {"message": "meters logs will be deleted here"}
#
#
# @router.delete("/delete/{id}")
# async def delete_log():
#     return {"message": str(id)+": this meter log will be deleted here"}
