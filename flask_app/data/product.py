import sqlalchemy
from .db_session import SqlAlchemyBase
from sqlalchemy import orm


class Product(SqlAlchemyBase):
    __tablename__ = 'products'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
    name = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    description = sqlalchemy.Column(sqlalchemy.String, nullable=True)
    quantity = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    price = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
#    purchase = orm.relation("Purchase", back_populates='products')

    def __repr__(self):
        return self.name
