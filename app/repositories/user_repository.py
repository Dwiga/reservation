from app.libs.database import CRUD


class UserRepository(CRUD):
    TABLE = "users"

    def __init__(self):
        super().__init__()
