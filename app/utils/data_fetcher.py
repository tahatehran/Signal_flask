import requests
from flask import current_app
from app import db
from app.models import CryptoData

def fetch_crypto_data():
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/listings/latest'
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': current_app.config['COINMARKETCAP_API_KEY'],
    }
    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()
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
        current_app.logger.info(f"Fetched and stored data for {len(data)} cryptocurrencies")
        return data
    except requests.RequestException as e:
        current_app.logger.error(f"Error fetching data from CoinMarketCap: {str(e)}")
        return None
