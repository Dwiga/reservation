from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordBearer

transaction = APIRouter(prefix="/transaction", tags=["transaction"], responses={404: {"description": "Not found"}})
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")


@transaction.post("/buy")
def buy(token: str = Depends(oauth2_scheme)):
    return "Buy"
