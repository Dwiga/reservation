from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer
from app.schemas.transaction_form import Buy, Book
from app.repositories.user_repository import UserRepository
from app.models.users import Users
from app.services.order_service import create_buy, create_book


transaction = APIRouter(prefix="/transaction", tags=["transaction"], responses={404: {"description": "Not found"}})
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@transaction.post("/buy")
def buy(form: Buy, token: str = Depends(oauth2_scheme)):
    user_repo = UserRepository()

    user: Users = user_repo.fetch_by_token(token)
    if not user:
        return {"message": "Invalid token"}

    return create_buy(form, user)


@transaction.post("/book")
def book(form: Book, token: str = Depends(oauth2_scheme)):
    user_repo = UserRepository()

    user: Users = user_repo.fetch_by_token(token)
    if not user:
        return {"message": "Invalid token"}

    return create_book(form, user)
