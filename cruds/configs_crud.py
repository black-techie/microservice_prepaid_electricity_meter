import datetime
from sqlalchemy.orm import Session
from models import configs_model, meter_model
from schemas import configs_schema


def get_configs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(configs_model.Config).offset(skip).limit(limit).all()


def get_config(db: Session, id: int):
    return db.query(configs_model.Config).get(id)


def create_config(db: Session, config: configs_schema.Config):
    now = str(datetime.datetime.now())
    meter = db.query(meter_model.Meter).filter(meter_model.Meter.id == config.meter_id).first()
    if meter:
        _config = configs_model.Config(
            configs=str(config.configs),
            status=False,
            meter_id=meter.id,
            modified_at=now,
            created_at=now
        )
        db.add(_config)
        db.commit()
        db.refresh(_config)
        return _config
    else:
        return {"message": "Meter not registered!"}


def update_config(db: Session, id: int, body: dict):
    body["modified_at"] = str(datetime.datetime.now())
    db.query(configs_model.Config).filter_by(id=id).update(body)
    db.commit()
    return db.query(configs_model.Config).get(id)


def delete_config(db: Session, id: int):
    meter = db.query(configs_model.Config).get(id)
    db.query(configs_model.Config).filter_by(id=id).delete()
    db.commit()
    return meter


def delete_all_configs(db: Session):
    status = db.query(configs_model.Config).delete()
    db.commit()
    return status
