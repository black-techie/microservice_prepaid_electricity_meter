from fastapi import APIRouter
from configs.database import SessionLocal
from cruds import configs_crud
from fastapi import Depends
from sqlalchemy.orm import Session
from schemas.configs_schema import Config

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@router.get("")
async def config_root():
    return {"message": "welcome to the index of the configs"}


@router.get("/id/{id}")
async def get_single_config(id: int, db: Session = Depends(get_db)):
    conf = configs_crud.get_config(db, id)
    return conf


@router.get("/all")
async def get_all_configs(db: Session = Depends(get_db)):
    conf = configs_crud.get_configs(db)
    return conf


@router.post("/create")
async def create_config(config: Config, db: Session = Depends(get_db)):
    conf = configs_crud.create_config(db, config)
    return conf


@router.patch("/update/{id}")
async def update_config(id: int, body: dict, db: Session = Depends(get_db)):
    conf = configs_crud.update_config(db, id, body)
    return conf


@router.delete("/delete/all")
async def delete_all_configs(db: Session = Depends(get_db)):
    rows = configs_crud.delete_all_configs(db)
    return {"message": f"{str(rows)} rows have been deleted!"}


@router.delete("/delete/{id}")
async def delete_config(id: int, db: Session = Depends(get_db)):
    conf = configs_crud.delete_config(db, id)
    return conf
