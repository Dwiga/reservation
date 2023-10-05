from datetime import datetime
from app.libs.database import CRUD
import numpy
from app.schemas.transaction_form import Buy, Book
from app.repositories.order_repository import OrderRepository
from app.models.users import Users
from app.models.orders import Orders
from app.models.tables import Tables
from app.models.seats import Seats
from app.repositories.table_repository import TableRepository
from app.repositories.seat_repository import SeatRepository
import random
import string


def create_buy(form: Buy, user: Users):
    order_repo = OrderRepository()
    table_repo = TableRepository()
    seat_repo = SeatRepository()

    date = datetime.strftime(form.date, "%Y-%m-%d")
    time = form.time

    seats = seat_repo.retrieve_all_seats()
    seat_ids = CRUD.pluck_id(seats)

    used_seats = seat_repo.retrieve_used_seats(time, date)
    used_seat_ids = CRUD.pluck_id(used_seats)

    available_seats = numpy.setdiff1d(seat_ids, used_seat_ids)
    seat_given = available_seats.tolist()[0]
    seat: Seats = seat_repo.fetch_by_id(seat_given)
    table: Tables = table_repo.fetch_by_id(seat.table_id)
    transaction_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

    order_data = Orders(
        type=0,
        user_id=user.id,
        table_id=table.id,
        seat_id=seat_given,
        price=table.price / 2,
        status=0,
        transaction_code=transaction_code,
        approved=False,
        created_at=datetime.now(),
        updated_at=datetime.now(),
        time=time,
        date=date,
    )
    order_repo.create(order_data)
    return order_data


def create_book(form: Book, user: Users):
    table_repo = TableRepository()
    seat_repo = SeatRepository()
    order_repo = OrderRepository()

    date = datetime.strftime(form.date, "%Y-%m-%d")
    time = form.time

    table: Tables = table_repo.fetch_by_id(form.table)
    seats = seat_repo.retrieve_by_table(table.id)
    transaction_code = ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))

    for seat in seats:
        order_data = Orders(
            type=1,
            user_id=user.id,
            table_id=table.id,
            seat_id=seat.id,
            price=table.price,
            status=0,
            transaction_code=transaction_code,
            approved=False,
            created_at=datetime.now(),
            updated_at=datetime.now(),
            time=time,
            date=date,
        )
        order_repo.create(order_data)
