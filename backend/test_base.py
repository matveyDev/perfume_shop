from sqlalchemy import create_engine, select
from sqlalchemy.orm import Session, Query

from database.local_db import SQLALCHEMY_DATABASE_URL


class BaseTest:
    def setup(self):
        self.engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.session = Session(self.engine)

    def teardown(self, models: list):
        queries = self._create_simple_queries(models)
        for query in queries:
            for item in self.session.scalars(query):
                self.session.delete(item)
                self.session.commit()

        for model in models:
            rows = [row for row in self.session.scalars(select(model))]
            assert len(rows) == 0, f'Table {model} is NOT empty!'

    def _create_simple_queries(self, models: list) -> list[Query]:
        queries = list()
        for model in models:
            query = select(model)
            queries.append(query)

        return queries
