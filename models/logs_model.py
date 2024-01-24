from sqlalchemy import Column, Integer, String, Float, ForeignKey
from configs.database import Base
from sqlalchemy.orm import relationship


class Log(Base):
    __tablename__ = "logs_"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    voltage = Column(Float, index=True)
    power = Column(Float, index=True)
    units = Column(Float, index=True)
    alerts = Column(String, index=True)
    params = Column(String, index=True)
    response = Column(String, index=True)
    datetime = Column(String, index=True)
    meter_id = Column(Integer, ForeignKey("meter__04.id"))
    meter = relationship("Meter", back_populates="logs")
