import aiohttp
from os import getenv
from fastapi import HTTPException

# Obtém a chave da API do Alpha Vantage das variáveis de ambiente
ALPHAVANTAGE_APIKEY = getenv('ALPHAVANTAGE_APIKEY')

async def async_converter(from_currency: str, to_currency: str, price: float):
    # Constrói a URL da API com os parâmetros fornecidos
    url = f'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency={from_currency}&to_currency={to_currency}&apikey={ALPHAVANTAGE_APIKEY}'

    try:
        # Cria uma sessão HTTP assíncrona
        async with aiohttp.ClientSession() as session:
            # Faz uma requisição GET à API
            async with session.get(url=url) as response:
                # Converte a resposta para JSON
                data = await response.json()
    except Exception as error:
        # Em caso de erro, lança uma exceção HTTP com status 400
        raise HTTPException(status_code=400, detail=str(error))
    
    # Verifica se a resposta contém a taxa de câmbio
    if 'Realtime Currency Exchange Rate' not in data:
        # Se não, lança uma exceção HTTP com status 400
        raise HTTPException(status_code=400, detail='Invalid response from Alpha Vantage API')
    
    # Obtém a taxa de câmbio dos dados recebidos
    exchange_rate = float(data['Realtime Currency Exchange Rate']['5. Exchange Rate'])
    
    # Retorna o valor convertido
    return {to_currency: price * exchange_rate}
