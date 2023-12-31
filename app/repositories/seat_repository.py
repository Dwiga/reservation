from app.libs.database import CRUD
from app.libs.connection import connection
from app.models.seats import Seats
from sqlmodel import select


class SeatRepository(CRUD):
    TABLE = Seats
    c = connection

    def __init__(self):
        super().__init__()

    def retrieve_all_seats(self):
        statement = "select s.* from seats as s left join orders as o on s.id = o.seat_id"
        return self.c.execute(statement).all()

    def retrieve_used_seats(self, time: int, date: str):
        statement = ("select s.* from seats as s left join orders as o on s.id = o.seat_id where o.time = {} and "
                     "text(o.date) like '{}%'".format(time, date))
        return self.c.execute(statement).all()

    def retrieve_by_table(self, table_id: int):
        statement = select(self.TABLE).where(self.TABLE.table_id == table_id)
        resultset = connection.exec(statement)
        return resultset.all()
