from sqlalchemy import select

from query_base import BaseQueries
from database.base import Perfume
from .schemas import Perfume as PerfumeSchema


class PerfumeQueries(BaseQueries):

    def get_perfumes_by_brand(self, brand: str) -> list[PerfumeSchema]:
        perfumes_query = select(Perfume).where(
            Perfume.brand==brand
        )
        perfumes = self.session.scalars(perfumes_query)
        perfumes_list = [perfume.__dict__ for perfume in perfumes]

        return perfumes_list
