from app import db
from datetime import datetime

class CryptoData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    symbol = db.Column(db.String(10), index=True)
    price = db.Column(db.Float)
    volume_24h = db.Column(db.Float)
    percent_change_24h = db.Column(db.Float)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f'<CryptoData {self.symbol}>'

    def to_dict(self):
        return {
            'id': self.id,
            'symbol': self.symbol,
            'price': self.price,
            'volume_24h': self.volume_24h,
            'percent_change_24h': self.percent_change_24h,
            'timestamp': self.timestamp.isoformat()
        }
