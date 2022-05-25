from sqlalchemy import select

from test_base import BaseTest
from database.base import Cart, User


class TestCartModel(BaseTest):
    def setup(self):
        super().setup()
        self.teardown()

        self.create_users()
        self.create_carts()

    def create_users(self):
        self.user_1 = User(
            email='example123@example.com',
            first_name='TestFirstName1',
            last_name='TestLastName1',
            username='test1',
            hashed_password='hashedpass123',
        )
        self.user_2 = User(
            email='example321@example.com',
            first_name='TestFirstName2',
            last_name='TestLastName2',
            username='test2',
            hashed_password='hashedpass123',
        )
        self.session.add_all([self.user_1, self.user_2])
        self.session.commit()

    def create_carts(self):
        self.cart_1 = Cart(
            user_id=self.user_1.id
        )
        self.cart_2 = Cart(
            user_id=self.user_2.id
        )
        self.session.add_all([self.cart_1, self.cart_2])
        self.session.commit()

    def test_cart(self):
        carts = self.session.scalars(select(Cart))
        assert len([cart for cart in carts]) == 2

        for cart in carts:
            if cart == self.cart_1:
                assert cart.user == self.user_1
                assert cart.user_id == self.user_1.id
            if cart == self.cart_2:
                assert cart.user == self.user_2
                assert cart.user_id == self.user_2.id

    def teardown(self):
        models = [Cart, User]
        super().teardown(models)
