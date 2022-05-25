from fastapi import APIRouter, HTTPException, Query, Path
from typing import Optional

from .queries import PerfumeQueries
from .schemas import Perfume

router = APIRouter(
    prefix='/perfume',
    tags=['perfume']
)

perfume_queries = PerfumeQueries()

# @router.get('/brand')
# async def get_brands():


@router.get('/{brand}', response_model=list[Perfume])
async def get_perfume_by_brand(
    brand: str = Path(..., title='The perfume\'s brand'),
    limit: Optional[int] = Query(None, title='Limit of perfumes'),
):
    brand = brand.replace('_', ' ').replace('-', ' ').title()
    perfumes = perfume_queries.get_perfumes_by_brand(brand)

    if len(perfumes) == 0:
        return HTTPException(404)

    if (limit is not None) and len(perfumes) > limit:
        perfumes = perfumes[0:limit]

    return perfumes
