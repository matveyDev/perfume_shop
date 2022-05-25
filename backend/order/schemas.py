from datetime import datetime
from pydantic import BaseModel



class Order(BaseModel):
    id: int
    discount: int
    datetime: datetime
    shipped: bool
    total_cost: float
    tracking_number: str
    perfume_ids: list[int]
    user_id: int

    class Config:
        schema_extra = {
            'example': {
                'id': 3,
                'discount': 10,
                'datetime': datetime.now(),
                'shipped': True,
                'total_cost': 177.22,
                'tracking_number': 'RR123456789RU',
                'perfume_ids': [2, 2, 5, 50],
                'user_id': 5,
            }
        }
