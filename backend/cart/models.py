from database.db import Base

from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship


class Cart(Base):
    __tablename__ = 'cart'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='cart')

    perfumes_in_cart = relationship('PerfumeInCart', back_populates='cart')

    def __repr__(self) -> str:
        return f'<Cart {self.id}>'
