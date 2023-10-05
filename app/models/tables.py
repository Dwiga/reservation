from sqlmodel import SQLModel, Field, Relationship, func
from datetime import datetime
from typing import Optional, List


class Tables(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    number: int = Field()
    created_at: datetime = Field(default=func.now())
    updated_at: datetime = Field(default=func.now())
    price: float = Field(default=0.0)

    seats: Optional[List["Seats"]] = Relationship(back_populates="tables")
