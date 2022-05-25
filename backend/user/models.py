from database.db import Base

from sqlalchemy import Column, String, Integer, Boolean
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    first_name = Column(String(255), nullable=False)
    last_name = Column(String(255), nullable=False)
    email = Column(String(255), nullable=False)
    username = Column(String(25), nullable=False, unique=True)
    hashed_password = Column(String(100), nullable=False)
    order_counter = Column(Integer, default=0)
    super_user = Column(Boolean, default=False)

    cart = relationship('Cart', back_populates='user', uselist=False)
    orders = relationship('Order', back_populates='user')

    def __repr__(self) -> str:
        return f'<User {self.id}>'
