



#Como? Acompanhar a cotação das criptos.


import json
from requests import Session
from requests.exceptions import ConnectionError
from requests.exceptions import Timeout, TooManyRedirects

def cotacao():

    sua_api_key =                                                                                 "64994445-d3b2-42aa-8660-94cd653cfda6"  

    url = """
    https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest"""

    parameters = {
        "start":"1",
        "limit":"100",
        "convert":"USD"
    }

    headers = {
        "Accepts":"application/json",
        "X-CMC_PRO_API_KEY": sua_api_key
    }

    session = Session()
    session.headers.update(headers)

    try: 
        response = session.get(url,params=parameters)
        data_full = json.loads(response.text)["data"]
        dicionario_de_criptos = {}

        for data in data_full:
            simbolo_da_criptomoeda = data["symbol"]
            preco_da_criptomoeda = data["quote"]["USD"]["price"]

            dicionario_de_criptos[simbolo_da_criptomoeda] = preco_da_criptomoeda
        
        return dicionario_de_criptos

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)