from app.libs.database import CRUD


class TableRepository(CRUD):
    TABLE = "tables"

    def __init__(self):
        super().__init__()
