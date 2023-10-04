from sqlmodel import SQLModel, Field, Relationship, func
from datetime import datetime, date, time
from typing import Optional
from app.models.users import Users
from app.models.tables import Tables
from app.models.seats import Seats


class Orders(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    type: int = Field(default=0)
    user_id: int = Field(default=None, foreign_key="users.id")
    table_id: int = Field(default=None, foreign_key="tables.id")
    seat_id: int = Field(default=None, foreign_key="seats.id")
    price: float = Field(default=0.0)
    status: int = Field(default=0)
    transaction_code: str = Field(default=None)
    approved: bool = Field(default=False)
    time: datetime = Field(default=func.now())
    created_at: datetime = Field(default=func.now())
    updated_at: datetime = Field(default=func.now())

    users: Optional[Users] = Relationship(back_populates="orders")
    tables: Optional[Tables] = Relationship(back_populates="orders")
    seats: Optional[Seats] = Relationship(back_populates="orders")
