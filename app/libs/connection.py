from sqlmodel import SQLModel, create_engine, Session
from app.libs.config import database

DATABASE_URL = database()

engine = create_engine(DATABASE_URL, echo=True)

connection = Session(engine)


def create_db_and_tables():
    SQLModel.metadata.create_all(engine)
