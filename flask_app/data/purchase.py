import sqlalchemy
from sqlalchemy import orm

from .db_session import SqlAlchemyBase


class Purchase(SqlAlchemyBase):
    __tablename__ = 'purchase'

    id = sqlalchemy.Column(sqlalchemy.Integer,
                           primary_key=True, autoincrement=True)
#    user_id = sqlalchemy.Column(sqlalchemy.Integer,
#                                sqlalchemy.ForeignKey("users.id"))
#    user = orm.relation('User')
#    product_id = sqlalchemy.Column(sqlalchemy.Integer,
#                                   sqlalchemy.ForeignKey("products.id"))
#    product = orm.relation('Product')
    count = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    amount = sqlalchemy.Column(sqlalchemy.Integer, nullable=True)
    address = sqlalchemy.Column(sqlalchemy.String, nullable=True)
