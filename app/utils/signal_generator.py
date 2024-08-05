from app.models import CryptoData
from flask import current_app

def generate_signals():
    try:
        cryptos = CryptoData.query.order_by(CryptoData.timestamp.desc()).limit(100).all()
        signals = []

        for crypto in cryptos:
            if crypto.percent_change_24h > 5:
                signals.append({'symbol': crypto.symbol, 'signal': 'BUY'})
            elif crypto.percent_change_24h < -5:
                signals.append({'symbol': crypto.symbol, 'signal': 'SELL'})
            else:
                signals.append({'symbol': crypto.symbol, 'signal': 'HOLD'})

        current_app.logger.info(f"Generated {len(signals)} trading signals")
        return signals
    except Exception as e:
        current_app.logger.error(f"Error generating trading signals: {str(e)}")
        return None
