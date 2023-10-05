from app.libs.database import CRUD
from app.libs.connection import connection
from sqlmodel import select
from app.models.users import Users


class UserRepository(CRUD):
    TABLE = Users

    def __init__(self):
        super().__init__()

    def fetch_by_username(self, username: str):
        statement = select(self.TABLE).where(self.TABLE.username == username)
        query = connection.exec(statement)
        return query.first()

    def fetch_by_token(self, token: str):
        statement = select(self.TABLE).where(self.TABLE.token == token)
        query = connection.exec(statement)
        return query.first()
