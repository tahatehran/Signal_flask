from flask import jsonify, current_app
from app.api import bp
from app.utils.data_fetcher import fetch_crypto_data
from app.utils.price_predictor import predict_prices
from app.utils.signal_generator import generate_signals

@bp.route('/data')
def get_data():
    data = fetch_crypto_data()
    if data is None:
        return jsonify({'error': 'Failed to fetch data'}), 500

    prediction = predict_prices()
    signals = generate_signals()

    response = {
        'data': data,
        'prediction': prediction,
        'signals': signals
    }

    return jsonify(response)
