from typing import Union, List
from fastapi import APIRouter, HTTPException, Query, Path

from .crud import CRUDPerfume
from .schemas import Perfume as PerfumeSchema

router = APIRouter(
    prefix='/perfume',
    tags=['perfume']
)

CRUD = CRUDPerfume()


@router.get('/{brand}', response_model=List[PerfumeSchema])
async def get_perfume_by_brand(
    brand: str = Path(..., title='The perfume\'s brand'),
    limit: Union[int, None] = Query(None, title='Limit of perfumes'),
):
    brand = brand.replace('_', ' ').replace('-', ' ').title()
    perfumes = CRUD.get_perfumes_by_brand(brand, limit)

    # Nothing to show
    if len(perfumes) == 0:
        return HTTPException(404)

    return perfumes
