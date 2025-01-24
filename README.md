# APITempoDIO

Este projeto utiliza FastAPI para criar uma API de tempo.

## Requisitos

- Python 3.7+
- FastAPI
- Uvicorn

## Instalação

1. Clone o repositório:

    ```bash
    git clone https://github.com/seu-usuario/APITempoDIO.git
    cd APITempoDIO
    ```

2. Crie um ambiente virtual e ative-o:

    ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows use `venv\Scripts\activate`
    ```

3. Instale as dependências:

    ```bash
    pip install -r requirements.txt
    ```

## Executando o Projeto

1. Inicie o servidor:

    ```bash
    uvicorn main:app --reload
    ```

## Endpoints

A API possui os seguintes endpoints:

- **GET /**: Retorna uma mensagem de boas-vindas.
- **GET /tempo**: Retorna a previsão do tempo atual.

## Exemplo de Uso

Para obter a previsão do tempo, faça uma requisição GET para o endpoint `/tempo`:

```bash
curl -X 'GET' \
    'http://127.0.0.1:8000/tempo' \
    -H 'accept: application/json'
```

A resposta será no formato JSON:

```json
{
    "cidade": "São Paulo",
    "temperatura": "25°C",
    "descricao": "Parcialmente nublado"
}
```