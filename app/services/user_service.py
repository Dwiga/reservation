from app.models.users import Users
from app.repositories.user_repository import UserRepository
import bcrypt


def create_user(user: Users):
    salt = bcrypt.gensalt()

    user_repo = UserRepository()
    user.password = bcrypt.hashpw(user.password.encode(), salt)
    result: Users = user_repo.create(user)
    return result
