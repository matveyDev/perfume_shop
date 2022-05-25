from sqlalchemy import select

from test_base import BaseTest
from database.base import Cart, User, Order,\
    Perfume, PerfumeInCart, PerfumeInOrder


class PerfumeBaseTest(BaseTest):

    def create_perfumes(self):
        self.perfume_1 = Perfume(
            brand='Test Test1',
            name='test1',
            description='test desc1',
            price=77.77
        )
        self.perfume_2 = Perfume(
            brand='Test Test2',
            name='test2',
            description='test desc2',
            price=77.77
        )
        self.session.add_all([self.perfume_1, self.perfume_2])
        self.session.commit()

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


class TestPerfumeInOrderModel(PerfumeBaseTest):
    def setup(self):
        self.models = [User, Cart, PerfumeInOrder, Perfume]
        super().setup()
        self.teardown()

        self.create_perfumes()
        self.create_users()
        self.create_orders()
        self.create_perfumes_in_order()

    def create_perfumes_in_order(self):
        self.perfume_1_in_order_1 = PerfumeInOrder(
            order_id=self.order_1.id,
            perfume_id=self.perfume_1.id
        )
        self.perfume_2_in_order_1 = PerfumeInOrder(
            order_id=self.order_1.id,
            perfume_id=self.perfume_2.id
        )
        self.perfume_1_in_order_2 = PerfumeInOrder(
            order_id=self.order_2.id,
            perfume_id=self.perfume_1.id
        )
        self.perfume_2_in_order_2 = PerfumeInOrder(
            order_id=self.order_2.id,
            perfume_id=self.perfume_2.id
        )
        
        self.session.add_all(
            [self.perfume_1_in_order_1, self.perfume_2_in_order_1,
             self.perfume_1_in_order_2, self.perfume_2_in_order_2]
        )
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
            user_id=self.user_2.id
        )
        self.session.add_all([self.order_1, self.order_2])
        self.session.commit()

    def test_perfume_in_order(self):
        perfumes_in_order = self.session.scalars(select(PerfumeInOrder))
        assert len([i for i in perfumes_in_order]) == 4

        perfumes_in_order_1 = self.session.scalars(
            select(PerfumeInOrder)
            .where(
                PerfumeInOrder.order_id==self.order_1.id,
            )
        )
        perfumes_in_order_2 = self.session.scalars(
            select(PerfumeInOrder)
            .where(
                PerfumeInOrder.order_id==self.order_2.id,
            )
        )
        assert len([i for i in perfumes_in_order_1]) == 2
        assert len([i for i in perfumes_in_order_2]) == 2

        for perfume in perfumes_in_order_1:
            assert perfume.order_id == self.order_1.id
            assert perfume.perfume_id in [self.perfume_1.id, self.perfume_2.id]

        for perfume in perfumes_in_order_2:
            assert perfume.order_id == self.order_2.id
            assert perfume.perfume_id in [self.perfume_1.id, self.perfume_2.id]

    def teardown(self):
        super().teardown(self.models)


class TestPerfumeInCartModel(PerfumeBaseTest):
    def setup(self):
        self.models = [User, Cart, PerfumeInCart, Perfume]
        super().setup()
        self.create_queries()
        self.teardown()

        self.create_perfumes()
        self.create_users()
        self.create_carts()
        self.create_perfumes_in_cart()

    def create_perfumes_in_cart(self):
        self.perfume_1_in_cart_1 = PerfumeInCart(
            cart_id=self.cart_1.id,
            perfume_id=self.perfume_1.id,
        )
        self.perfume_2_in_cart_1 = PerfumeInCart(
            cart_id=self.cart_1.id,
            perfume_id=self.perfume_2.id
        )

        self.perfume_1_in_cart_2 = PerfumeInCart(
            cart_id=self.cart_2.id,
            perfume_id=self.perfume_1.id
        )
        self.perfume_2_in_cart_2 = PerfumeInCart(
            cart_id=self.cart_2.id,
            perfume_id=self.perfume_2.id
        )

        self.session.add_all(
            [self.perfume_1_in_cart_1, self.perfume_2_in_cart_1,
             self.perfume_1_in_cart_2, self.perfume_2_in_cart_2]
        )
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

    def create_queries(self):
        self.queries = self._create_simple_queries(
            models=self.models
        )

    def test_perfume_in_cart(self):
        perfumes_in_cart = self.session.scalars(select(PerfumeInCart))
        assert len([i for i in perfumes_in_cart]) == 4, len([i for i in perfumes_in_cart])

        perfumes_in_cart_1 = self.session.scalars(
            select(PerfumeInCart)
            .where(
                PerfumeInCart.cart_id==self.cart_1.id,
            )
        )
        perfumes_in_cart_2 = self.session.scalars(
            select(PerfumeInCart)
            .where(
                PerfumeInCart.cart_id==self.cart_2.id,
            )
        )
        assert len([i for i in perfumes_in_cart_1]) == 2
        for perfume in perfumes_in_cart_1:
            assert perfume.cart_id == self.cart_1.id
            assert perfume.perfume_id in [self.perfume_1.id, self.perfume_2.id]

        assert len([i for i in perfumes_in_cart_2]) == 2
        for perfume in perfumes_in_cart_2:
            assert perfume.cart_id == self.cart_2.id
            assert perfume.perfume_id in [self.perfume_1.id, self.perfume_2.id]

    def teardown(self):
        super().teardown(self.models)


class aTestPerfumeModel(PerfumeBaseTest):
    def setup(self):
        super().setup()

        self.create_queries()
        self.teardown()

        self.create_perfumes()

    def create_queries(self):
        self.query_perfumes = select(Perfume)

    def test_perfume(self):
        perfumes = self.session.scalars(self.query_perfumes)

        assert len([i for i in perfumes]) == 2, len([i for i in perfumes])

        for perfume in perfumes:
            assert perfume.quantity == 5, perfume.quantity
            assert perfume.milliliters == 100, perfume.milliliters
            assert perfume.available is True, perfume.available
            assert perfume.visible is True, perfume.visible
            assert perfume.price == 77.77, perfume.price

    def teardown(self):
        models = [Perfume, ]
        super().teardown(models)
