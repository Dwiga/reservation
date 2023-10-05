from app.models.users import Users
from app.repositories.user_repository import UserRepository
import bcrypt


def create_user(user: Users):
    salt = bcrypt.gensalt()
    password = user.password
    password_bytes = password.encode('utf-8')
    password_hash = bcrypt.hashpw(password_bytes, salt)

    user_repo = UserRepository()
    user.password = password_hash.decode()
    result: Users = user_repo.create(user)
    return result
