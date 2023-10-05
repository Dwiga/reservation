from app.models.tables import Tables
from app.repositories.table_repository import TableRepository


def create_table(table: Tables) -> Tables:
    table_repo = TableRepository()
    result: Tables = table_repo.create(table)
    return result
