from sqlalchemy import select

from test_base import BaseTest
from database.base import Order, User


class TestUserModel(BaseTest):

    def setup(self):
        super().setup()

        self.create_users()
        self.create_queries()
        self.create_order()

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

    def create_order(self):
        self.order_1 = Order(
            perfume_ids='1, 2',
            user_id=self.user_1_id,
            total_cost=110.11
        )
        self.order_2 = Order(
            perfume_ids='3, 2',
            user_id=self.user_1_id,
            total_cost=200.11
        )
        self.session.add_all([self.order_1, self.order_2])
        self.session.commit()

    def create_queries(self):
        self.query_user_1 = select(User).where(User.username=='test1')

        self.query_users = select(User).where(User.username.in_(['test1', 'test2']))
        self.user_1_id = self.session.scalar(self.query_user_1).id
        self.query_orders = select(Order)

    def test_create(self):
        for user in self.session.scalars(self.query_users):
            assert user.username in ['test1', 'test2'], user.username
                
    def test_user_with_orders(self):
        user_1 = self.session.scalar(self.query_user_1)
        for order in user_1.orders:
            assert order.user_id == user_1.id
            assert order.user_id == self.user_1_id

        for order in self.session.scalars(self.query_orders):
            assert order.user_id == self.user_1_id

    def teardown(self):
        models=[User, Order]
        super().teardown(models)
