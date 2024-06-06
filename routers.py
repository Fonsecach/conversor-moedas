from fastapi import APIRouter, Path, Query
from conveter import async_converter
from asyncio import gather
from schamas import ConverterInput, ConverterOutput

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

# conversao de moedas de uma unidade a outras passando o parametro pelo body
@router.get('/converter/v2/{from_currency}', response_model=ConverterOutput)
async def converter(
    body: ConverterInput,
    from_currency: str = Path(max_length=3,regex='^[A-Z]{3}$'),

):
    to_currencies = body.to_currencies
    price = body.price
    
    couroutines = []
    
    for currency in to_currencies:
        coro = async_converter(
            from_currency=from_currency,
            to_currency = currency,
            price = price
        )
        
        couroutines.append(coro)
    
    result = await gather(*couroutines)
    return ConverterOutput(
        mensagem='sucess',
        data=result)

