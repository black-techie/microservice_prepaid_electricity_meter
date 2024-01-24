import random
import datetime
from sqlalchemy.orm import Session
from models import meter_model
from schemas import meter_schema


def get_meters(db: Session, skip: int = 0, limit: int = 100):
    return db.query(meter_model.Meter).offset(skip).limit(limit).all()


def get_meter(db: Session, id: int):
    return db.query(meter_model.Meter).get(id)


def create_meter(db: Session, meter: meter_schema.Meter):
    now = str(datetime.datetime.now())
    db_meter = meter_model.Meter(
        serial_number=meter.serial_number,
        api_key="{0}{1}".format(str(hex(int(datetime.datetime.now().strftime('%Y%m%d%H%M%S%f')))),
                                str(random.randint(456421003, 992981003))),
        no_of_phase=meter.no_of_phase,
        meter_type=meter.meter_type,
        max_current=meter.max_current,
        owner_id=meter.owner_id,
        owner_name=meter.owner_name,
        cellphone=meter.cellphone,
        municipal=meter.municipal,
        tarrif=meter.tarrif,
        units=meter.units,
        other=meter.other,
        modified_at=now,
        created_at=now
    )
    db.add(db_meter)
    db.commit()
    db.refresh(db_meter)
    return db_meter


def update_meter(db: Session, id: int, body: dict):
    body["modified_at"] = str(datetime.datetime.now())
    db.query(meter_model.Meter).filter_by(id=id).update(body)
    db.commit()
    return db.query(meter_model.Meter).get(id)


def delete_meter(db: Session, id: int):
    meter = db.query(meter_model.Meter).get(id)
    db.query(meter_model.Meter).filter_by(id=id).delete()
    db.commit()
    return meter


def delete_all(db: Session):
    status = db.query(meter_model.Meter).delete()
    db.commit()
    return status
