from app.libs.database import CRUD


class SeatRepository(CRUD):
    TABLE = "seats"

    def __init__(self):
        super().__init__()
