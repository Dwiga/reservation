from sqlmodel import SQLModel, Field, func, Relationship
from datetime import datetime
from typing import Optional, List


class Users(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True, index=True)
    name: str = Field()
    username: str = Field()
    password: str = Field()
    role: int = Field(default=0)
    created_at: datetime = Field(default=func.now())
    updated_at: datetime = Field(default=func.now())
    token: str = Field(nullable=True)

    orders: Optional[List["Orders"]] = Relationship(back_populates="users")
