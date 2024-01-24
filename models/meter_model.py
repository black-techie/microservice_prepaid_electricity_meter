from sqlalchemy import Column, Integer, String
from configs.database import Base
from sqlalchemy.orm import relationship


class Meter(Base):
    __tablename__ = "meter__04"
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    serial_number = Column(Integer, unique=True, index=True)
    meter_type = Column(String, unique=False, index=True)
    api_key = Column(String, unique=True, index=True)
    no_of_phase = Column(Integer, unique=False, index=True)
    max_current = Column(Integer, unique=False,  index=True)
    owner_id = Column(String, unique=True, index=True)
    owner_name = Column(String, unique=False, index=True)
    cellphone = Column(Integer, unique=False, index=True)
    municipal = Column(String, unique=False, index=True)
    tarrif = Column(String, unique=False, index=True)
    units = Column(Integer, unique=False, index=True)
    other = Column(String, unique=False, index=True)
    logs = relationship("Log", back_populates="meter")
    configs = relationship("Config", back_populates="meter")
    created_at = Column(String, index=True)
    modified_at = Column(String, index=True)

