from pydantic import BaseModel
from datetime import date


class Buy(BaseModel):
    time: int
    date: date
