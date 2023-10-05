from app.libs.database import CRUD
from app.models.orders import Orders
from app.libs.connection import connection


class OrderRepository(CRUD):
    TABLE = Orders
    c = connection

    def __init__(self):
        super().__init__()
