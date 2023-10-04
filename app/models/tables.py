from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional, List


class Tables(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    number: int = Field()
    created_at: datetime = Field()
    updated_at: datetime = Field()

    seats: Optional[List["Seats"]] = Relationship(back_populates="tables")
