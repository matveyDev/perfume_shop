from database.db import Base

from sqlalchemy_imageattach.entity import Image, image_attachment
from sqlalchemy import Column, String, Integer, Boolean, Float, ForeignKey
from sqlalchemy.orm import relationship


class PerfumeInOrder(Base):
    __tablename__ = 'perfume_in_order'
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    order_id = Column(Integer, ForeignKey('order.id'), unique=False, nullable=True)
    order = relationship('Order', back_populates='perfumes_in_order')

    perfume_id = Column(Integer, ForeignKey('perfume.id'), unique=False)
    perfume = relationship('Perfume', back_populates='perfume_in_order')

    def __repr__(self) -> str:
        return f'<PerfumeInOrder {self.id}>'


class PerfumeInCart(Base):
    __tablename__ = 'perfume_in_cart'
    
    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)

    cart_id = Column(Integer, ForeignKey('cart.id'), unique=False, nullable=True)
    cart = relationship('Cart', back_populates='perfumes_in_cart')

    perfume_id = Column(Integer, ForeignKey('perfume.id'), unique=False)
    perfume = relationship('Perfume', back_populates='perfume_in_cart')

    def __repr__(self) -> str:
        return f'<PerfumeInCart {self.id}>'


class Perfume(Base):
    __tablename__ = 'perfume'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    brand = Column(String(100), index=True)
    name = Column(String(100), unique=True)
    description = Column(String(5000))
    quantity = Column(Integer, default=5)
    milliliters = Column(Integer, default=100)
    available = Column(Boolean, default=True)
    visible = Column(Boolean, default=True)
    price = Column(Float, nullable=False)

    perfume_in_cart = relationship('PerfumeInCart', back_populates='perfume', uselist=False)
    perfume_in_order = relationship('PerfumeInOrder', back_populates='perfume', uselist=False)
    images = image_attachment('PerfumeImage', uselist=True, lazy='select', back_populates='perfume')

    def __repr__(self) -> str:
        return f'<Perfume {self.id}>'


class PerfumeImage(Base, Image):
    __tablename__ = 'perfume_images'

    id = Column(Integer, primary_key=True, index=True, unique=True, autoincrement=True)
    image_url = Column(String)
    perfume_id = Column(Integer, ForeignKey('perfume.id'), unique=False)
    perfume = relationship('Perfume', back_populates='images')
