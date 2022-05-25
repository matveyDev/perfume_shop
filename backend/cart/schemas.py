from pydantic import BaseModel


class Cart(BaseModel):
    id: int
    user_id: int

    class Config:
        schema_extra = {
            'example': {
                'id': 3,
                'user_id': 22,
            }
        }
