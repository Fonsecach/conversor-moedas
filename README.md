# API de conversão de moedas usando FastAPI e a API da Alpha Vantage

## Descrição

Este projeto é uma API para conversão de moedas usando FastAPI e a API da Alpha Vantage. Ele permite converter um valor de uma moeda para várias outras de forma assíncrona.

## Estrutura do Projeto

O projeto é composto pelos seguintes arquivos principais:

- `pyproject.toml`: Arquivo de configuração do Poetry para gerenciamento de dependências.
- `converter.py`: Contém a lógica para conversão de moedas utilizando a API da Alpha Vantage.
- `routers.py`: Define as rotas da API utilizando FastAPI.
- `main.py`: Ponto de entrada da aplicação FastAPI.

## Dependências

As dependências do projeto estão definidas no arquivo `pyproject.toml`. As principais são:

- Python 3.11
- aiohttp 3.9.5
- converter 1.0.0
- asyncio 3.4.3
- fastapi 0.111.0
- routers 0.10.1
- uvicorn 0.30.1

## Como Rodar

### Pré-requisitos

1. **Python 3.11**: Certifique-se de ter o Python 3.11 instalado em sua máquina.
2. **Poetry**: O Poetry é uma ferramenta para gerenciamento de dependências e pacotes no Python. Você pode instalá-lo seguindo as instruções no [site oficial](https://python-poetry.org/docs/#installation).

### Passos

1. **Clone o repositório**:

    ```bash
    git clone https://github.com/fonsecach/
    cd projeto1
    ```

2. **Instale as dependências**:

    ```bash
    poetry install
    ```

3. **Configure a chave da API da Alpha Vantage**:

    Crie um arquivo `.env` na raiz do projeto e adicione sua chave de API da Alpha Vantage:

    ```env
    ALPHAVANTAGE_APIKEY=your_api_key_here
    ```

4. **Execute a aplicação**:

    Para rodar a aplicação, utilize o Uvicorn, que é um servidor ASGI rápido:

    ```bash
    poetry run uvicorn main:app --reload
    ```

5. **Acesse a API**:

    A aplicação estará rodando em `http://127.0.0.1:8000`. Você pode acessar a documentação automática da API em `http://127.0.0.1:8000/docs`.

## Endpoints da API

### `GET /`

Retorna uma mensagem de boas-vindas.

#### Resposta:

```json
{
    "Hello": "World"
}
