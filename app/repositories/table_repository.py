from app.libs.database import CRUD
from app.models.tables import Tables


class TableRepository(CRUD):
    TABLE = Tables

    def __init__(self):
        super().__init__()
