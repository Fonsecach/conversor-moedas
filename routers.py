from fastapi import APIRouter, Path, Query
from conveter import async_converter
from asyncio import gather

router = APIRouter()

@router.get('/converter/{from_currency}')
async def converter(
    from_currency: str = Path(max_length=3,regex='^[A-Z]{3}$'),
    to_currencies: str = Query(max_length=50,regex='^[A-Z]{3}(,[A-Z]{3})*$'),
    price: float = Query(..., ge=0)
):
    to_currencies = to_currencies.split(',')
    
    couroutines = []
    
    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency = currency,
            price = price
        )
        
        couroutines.append(coro)
    
    result = await gather(*couroutines)
    return result

