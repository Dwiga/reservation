from app.libs.connection import connection
from sqlmodel import select


class CRUD:
    TABLE = "table"

    def __init__(self):
        pass

    @staticmethod
    def create(model):
        connection.add(model)
        connection.commit()
        return model

    # if you want multiple result sets
    # returns array : [{}]
    def retrieve(self, uid: str):
        statement = select(self.TABLE).where(self.TABLE.uid == uid)
        resultset = connection.exec(statement)
        return resultset.all()

    # if you expect one result set
    # returns dictionary : {}
    def fetch(self, id: int):
        statement = select(self.TABLE).where(self.TABLE.id == id)
        query = connection.exec(statement)
        return query.first()

    def fetch_by_id(self, uid: str):
        statement = select(self.TABLE).where(self.TABLE.uid == uid)
        query = connection.exec(statement)
        return query.first()

    def all(self):
        query = select(self.TABLE)
        result = connection.exec(query)
        return result.all()

    def delete(self, model):
        statement = select(self.TABLE).where(self.TABLE.id == model.id)
        result = connection.exec(statement)
        data = result.one()
        connection.delete(data)
        connection.commit()

    @staticmethod
    def update(model):
        connection.add(model)
        connection.commit()
