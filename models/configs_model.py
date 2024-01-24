from sqlalchemy import Column, Integer, String, ForeignKey, Boolean, JSON
from configs.database import Base
from sqlalchemy.orm import relationship


class Config(Base):
    __tablename__ = "configs__03"
    id = Column(Integer, primary_key=True, unique=True, index=True, autoincrement=True)
    configs = Column(String, primary_key=True, index=True)
    status = Column(Boolean, index=True)
    meter_id = Column(Integer, ForeignKey("meter__04.id"))
    meter = relationship("Meter", back_populates="configs")
    created_at = Column(String, index=True)
    modified_at = Column(String, index=True)
