from sqlalchemy import select

from test_base import BaseTest
from database.base import Order, User


class TestOrderModel(BaseTest):
    def setup(self):
        super().setup()
        self.teardown()

        self.create_users()
        self.create_orders()

    def create_users(self):
        self.user_1 = User(
            email='example123@example.exp',
            first_name='TestFirstName1',
            last_name='TestLastName1',
            username='test1',
            hashed_password='hashedpass123',
        )
        self.user_2 = User(
            email='example321@example.exp',
            first_name='TestFirstName2',
            last_name='TestLastName2',
            username='test2',
            hashed_password='hashedpass123',
        )
        self.session.add_all([self.user_1, self.user_2])
        self.session.commit()

    def create_orders(self):
        self.order_1 = Order(
            total_cost=110.50,
            perfume_ids='4,50',
            user_id=self.user_1.id
        )
        self.order_2 = Order(
            discount=50,
            shipped=True,
            tracking_number='RR123456789RU',
            total_cost=180.70,
            perfume_ids='1,66,78',
            user_id=self.user_1.id
        )
        self.order_3 = Order(
            total_cost=60.50,
            perfume_ids='9',
            user_id=self.user_2.id
        )
        self.session.add_all([self.order_1, self.order_2, self.order_3])
        self.session.commit()

    def test_order(self):
        orders = self.session.scalars(select(Order))
        assert len([order for order in orders]) == 3, 'Some order(s) has NOT been created'

        for order in orders:
            if order == self.order_1:
                assert order.discount == 0, order.discount
                assert order.shipped is False, order.shipped
                assert order.total_cost == 110.50, order.total_cost
                assert order.tracking_number == None, order.tracking_number
                assert order.perfume_ids == '4,50', order.perfume_ids
                assert order.user_id == self.user_1.id, order.user_id
                assert order.user == self.user_1

            if order == self.order_2:
                assert order.discount == 50, order.discount
                assert order.shipped is True, order.shipped
                assert order.total_cost == 180.70, order.total_cost
                assert order.tracking_number == 'RR123456789RU', order.tracking_number
                assert order.perfume_ids == '1,66,78', order.perfume_ids
                assert order.user_id == self.user_1.id, order.user_id
                assert order.user == self.user_1

            if order == self.order_3:
                assert order.discount == 0, order.discount
                assert order.shipped is False, order.shipped
                assert order.total_cost == 60.50, order.total_cost
                assert order.tracking_number == None, order.tracking_number
                assert order.perfume_ids == '9', order.perfume_ids
                assert order.user_id == self.user_1.id, order.user_id
                assert order.user == self.user_2

        users = self.session.scalars(select(User))
        for user in users:
            if user == self.user_1:
                assert len([order for order in user.orders]) == 2
            if user == self.user_2:
                assert len([order for order in user.orders]) == 1
                assert user.orders[0] == self.order_3

    def teardown(self):
        models = [Order, User]
        super().teardown(models)
