import numpy as np
from sklearn.ensemble import RandomForestRegressor
from app.models import CryptoData

def predict_prices():
    cryptos = CryptoData.query.order_by(CryptoData.timestamp.desc()).limit(1000).all()
    
    X = np.array([[c.volume_24h, c.percent_change_24h] for c in cryptos])
    y = np.array([c.price for c in cryptos])

    model = RandomForestRegressor(n_estimators=100)
    model.fit(X, y)

    latest_data = X[-1].reshape(1, -1)
    prediction = model.predict(latest_data)

    return prediction[0]
