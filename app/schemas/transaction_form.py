from pydantic import BaseModel
from datetime import date


class Buy(BaseModel):
    time: int
    date: date


class Book(BaseModel):
    time: int
    date: date
    table: int
