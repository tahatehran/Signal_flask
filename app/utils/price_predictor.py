import numpy as np
from sklearn.ensemble import RandomForestRegressor
from app.models import CryptoData
from flask import current_app

def predict_prices():
    try:
        cryptos = CryptoData.query.order_by(CryptoData.timestamp.desc()).limit(1000).all()
        
        if len(cryptos) < 100:
            current_app.logger.warning("Not enough data for prediction")
            return None

        X = np.array([[c.volume_24h, c.percent_change_24h] for c in cryptos])
        y = np.array([c.price for c in cryptos])

        model = RandomForestRegressor(n_estimators=100, random_state=42)
        model.fit(X, y)

        latest_data = X[-1].reshape(1, -1)
        prediction = model.predict(latest_data)

        current_app.logger.info(f"Price prediction: {prediction[0]}")
        return prediction[0]
    except Exception as e:
        current_app.logger.error(f"Error in price prediction: {str(e)}")
        return None
