from sqlmodel import SQLModel, Field, Relationship
from datetime import datetime
from typing import Optional
from app.models.tables import Tables


class Seats(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    number: int = Field()
    table_id: int = Field(foreign_key="tables.id")
    created_at: datetime = Field()
    updated_at: datetime = Field()

    tables: Optional[Tables] = Relationship(back_populates="seats")
