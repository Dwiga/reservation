from app.services.user_service import create_user
from app.models.users import Users
from sqlmodel import func


def user_seeding():
    admin = Users(
        name="John Doe",
        username="johndoe",
        password="password",
        role=0,
        created_at=func.now(),
        updated_at=func.now()
    )
    create_user(admin)

    customer = Users(
        name="John Doe",
        username="johndoe",
        password="password",
        role=1,
        created_at=func.now(),
        updated_at=func.now()
    )
    create_user(customer)
