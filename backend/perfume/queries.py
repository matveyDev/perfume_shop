from sqlalchemy import select, create_engine
from sqlalchemy.orm import Session

from .schemas import Perfume as PerfumeSchema
from database.base import Perfume
from database.local_db import SQLALCHEMY_DATABASE_URL


class PerfumeQueries:
    def __init__(self):
        engine = create_engine(SQLALCHEMY_DATABASE_URL)
        self.session = Session(engine)

    def get_perfumes_by_brand(self, brand: str) -> list[PerfumeSchema]:
        perfumes_query = select(Perfume).where(
            Perfume.brand==brand
        )
        perfumes = self.session.scalars(perfumes_query)
        perfumes_list = [perfume.__dict__ for perfume in perfumes]

        return perfumes_list
