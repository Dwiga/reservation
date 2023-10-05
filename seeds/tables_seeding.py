from app.models.tables import Tables
from app.models.seats import Seats
from sqlmodel import func
from app.repositories.table_repository import TableRepository
from app.repositories.seat_repository import SeatRepository


def table_seeding():
    tables = [
        Tables(
            number=1,
            created_at=func.now(),
            updated_at=func.now(),
            price=100.0
        ),
        Tables(
            number=2,
            created_at=func.now(),
            updated_at=func.now(),
            price=200.0
        ),
        Tables(
            number=3,
            created_at=func.now(),
            updated_at=func.now(),
            price=300.0
        ),
        Tables(
            number=4,
            created_at=func.now(),
            updated_at=func.now(),
            price=400.0
        )
    ]

    seats = [
        [
            Seats(
                number=1,
                table_id=1,
                created_at=func.now(),
                updated_at=func.now(),
            ),
            Seats(
                number=2,
                table_id=1,
                created_at=func.now(),
                updated_at=func.now(),
            )
        ],
        [
            Seats(
                number=3,
                table_id=2,
                created_at=func.now(),
                updated_at=func.now(),
            ),
            Seats(
                number=4,
                table_id=2,
                created_at=func.now(),
                updated_at=func.now(),
            )
        ],
        [
            Seats(
                number=5,
                table_id=3,
                created_at=func.now(),
                updated_at=func.now(),
            ),
            Seats(
                number=6,
                table_id=3,
                created_at=func.now(),
                updated_at=func.now(),
            )
        ],
        [
            Seats(
                number=7,
                table_id=4,
                created_at=func.now(),
                updated_at=func.now(),
            ),
            Seats(
                number=8,
                table_id=4,
                created_at=func.now(),
                updated_at=func.now(),
            )
        ]
    ]

    table_repo = TableRepository()
    seat_repo = SeatRepository()

    for i in range(len(tables)):
        table_repo.create(tables[i])
        for j in range(len(seats[i])):
            seat_repo.create(seats[i][j])
