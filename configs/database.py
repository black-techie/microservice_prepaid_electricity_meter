from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = ("postgresql://black:xmRfbG5FyKQ6qlCiPtYiaygBOw9brykl@dpg-ck7k7f7sasqs73b51cc0-a.singapore"
                           "-postgres.render.com/luxon_microservice_db")

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, pool_size=10, max_overflow=20
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
