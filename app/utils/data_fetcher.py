import requests
from app import db
from app.models import CryptoData
from config import Config

def fetch_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': Config.COINMARKETCAP_API_KEY,
    }
    response = requests.get(url, headers=headers)
    data = response.json()['data']

    for coin in data:
        crypto = CryptoData(
            symbol=coin['symbol'],
            price=coin['quote']['USD']['price'],
            volume_24h=coin['quote']['USD']['volume_24h'],
            percent_change_24h=coin['quote']['USD']['percent_change_24h']
        )
        db.session.add(crypto)
    
    db.session.commit()
    return data
