from datetime import datetime

from database.db import Base

from sqlalchemy import Column, String, Integer, Float, Boolean, ForeignKey, DateTime
from sqlalchemy.orm import relationship


class Order(Base):
    __tablename__ = 'order'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    discount = Column(Integer, default=0)
    datetime = Column(DateTime, default=datetime.now())
    shipped = Column(Boolean, default=False)
    total_cost = Column(Float, nullable=False)
    tracking_number = Column(String(50), default=None)
    perfume_ids = Column(String(255), nullable=False)

    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', back_populates='orders')

    perfumes_in_order = relationship('PerfumeInOrder', back_populates='order')

    def __repr__(self) -> str:
        return f'<Order {self.id}>'
