import datetime
from sqlalchemy.orm import Session
from models import logs_model, meter_model
from schemas import logs_schema


def get_logs(db: Session, skip: int = 0, limit: int = 100):
    return db.query(logs_model.Log).offset(skip).limit(limit).all()


def get_log(db: Session, id: int):
    return db.query(logs_model.Log).get(id)


def create_log(db: Session, log: logs_schema.Log):
    now = str(datetime.datetime.now())
    meter = db.query(meter_model.Meter).filter(meter_model.Meter.api_key == log.api_key).first()
    if meter:
        db_meter = logs_model.Log(
            voltage=log.voltage,
            power=log.power,
            units=log.units,
            alerts=log.alerts,
            params=log.params,
            response=log.response,
            datetime=now,
            meter_id=meter.id
        )
        db.add(db_meter)
        db.commit()
        db.refresh(db_meter)
        return meter.configs
    else:
        return {"message": "Meter not registered!"}


def update_log(db: Session, id: int, body: dict):
    body["modified_at"] = str(datetime.datetime.now())
    db.query(logs_model.Log).filter_by(id=id).update(body)
    db.commit()
    return db.query(logs_model.Log).get(id)


def delete_log(db: Session, id: int):
    meter = db.query(logs_model.Log).get(id)
    db.query(logs_model.Log).filter_by(id=id).delete()
    db.commit()
    return meter


def delete_all(db: Session):
    status = db.query(logs_model.Log).delete()
    db.commit()
    return status
