from crud_base import CRUDBase
from database.base import Perfume
from .schemas import Perfume as PerfumeSchema


class CRUDPerfume(CRUDBase):
    def __init__(self):
        super().__init__(Perfume)

    def get_perfumes_by_brand(self, brand: str, limit: int = None) -> list[PerfumeSchema]:
        brand = brand.replace('_', ' ').replace('-', ' ').title()
        query = self.session.query(Perfume).where(
            Perfume.brand==brand
        )
        if limit is not None:
            query = query.limit(limit)

        perfumes = self.session.scalars(query)
        perfumes_list = [perfume.__dict__ for perfume in perfumes]

        return perfumes_list

    # Create
    def add_perfume(self, perfume: PerfumeSchema) -> None:
        self.create(perfume)
