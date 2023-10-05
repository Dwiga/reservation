from app.libs.database import CRUD
from app.models.orders import Orders
from app.libs.connection import connection
from sqlmodel import select


class OrderRepository(CRUD):
    TABLE = Orders
    c = connection

    def __init__(self):
        super().__init__()

    def retrieve_by_order(self, order: str):
        statement = select(self.TABLE).where(self.TABLE.transaction_code == order)
        resultset = connection.exec(statement)
        return resultset.all()
