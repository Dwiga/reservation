from fastapi import APIRouter
from fastapi.security import OAuth2PasswordBearer
from app.schemas.auth_form import Login
import bcrypt
from app.models.users import Users
from app.repositories.user_repository import UserRepository
import random
import string

auth = APIRouter(prefix="/auth", tags=["auth"], responses={404: {"description": "Not found"}})
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@auth.post("/login")
def login(form_login: Login):
    user_repo = UserRepository()
    user: Users = user_repo.fetch_by_username(form_login.username)
    if not user:
        return {"message": "Invalid username or password"}
    if not bcrypt.checkpw(form_login.password.encode(), user.password.encode()):
        return {"message": "Invalid username or password"}
    user.token = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))
    user_repo.update(user)
    return {"token": user.token}
