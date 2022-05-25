from pydantic import BaseModel, EmailStr


class User(BaseModel):
    id: int
    email: EmailStr
    username: str
    order_counter: int
    super_user: bool
    cart_items: list[int]
    
    class Config:
        schema_extra = {
            'example': {
                'id': 2,
                'email': 'qwerty@example.com',
                'username': 'somename123',
                'order_counter': 1,
                'super_user': False,
                'cart_items': [1, 1, 2]
            }
        }
