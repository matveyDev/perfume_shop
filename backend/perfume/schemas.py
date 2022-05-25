from pydantic import BaseModel


class PerfumeInCart(BaseModel):
    id: int
    order_id: int
    perfume_id: int

    class Config:
        schema_extra = {
            'example': {
                'id': 33,
                'order_id': 77,
                'perfume_id': 7
            }
        }


class PerfumeInCart(BaseModel):
    id: int
    cart_id: int
    perfume_id: int

    class Config:
        schema_extra = {
            'example': {
                'id': 22,
                'cart_id': 77,
                'perfume_id': 1
            }
        }


class Perfume(BaseModel):
    id: int
    brand: str
    name: str
    description: str
    quantity: int
    milliliters: int
    available: bool
    visible: bool
    price: float

    class Config:
        schema_extra = {
            'example': {
                'id': 1,
                'brand': 'Tom Ford',
                'name': 'Lost Cherry',
                'description': 'some description...',
                'quantity': 4,
                'milliliters': 100,
                'available': True,
                'visible': True,
                'price': 77.77,
            }
        }


#ToDo: implement it
class PerfumeImages(BaseModel):
    'Implement me'
