from fastapi import APIRouter
from conveter import async_converter
from asyncio import gather

router = APIRouter()

@router.get('/converter/{from_currency}')
async def converter(from_currency: str, to_currencies: str, price: float):
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

