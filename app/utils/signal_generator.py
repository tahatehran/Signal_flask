from app.models import CryptoData

def generate_signals():
    cryptos = CryptoData.query.order_by(CryptoData.timestamp.desc()).limit(100).all()
    signals = []

    for crypto in cryptos:
        if crypto.percent_change_24h > 5:
            signals.append({'symbol': crypto.symbol, 'signal': 'BUY'})
        elif crypto.percent_change_24h < -5:
            signals.append({'symbol': crypto.symbol, 'signal': 'SELL'})
        else:
            signals.append({'symbol': crypto.symbol, 'signal': 'HOLD'})

    return signals
