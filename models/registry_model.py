from sqlalchemy import Column, Integer, String
from configs.database import Base


class Register(Base):
    __tablename__ = "registry"
    id = Column(Integer, primary_key=True, unique=False, index=True, autoincrement=True)
    admin = Column(String, index=True)
    ip_address = Column(String, index=True)
    method = Column(String, index=True)
    body = Column(Integer, unique=False, index=True)
    created_at = Column(String, index=True)
