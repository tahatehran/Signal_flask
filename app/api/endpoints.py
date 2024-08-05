from flask import jsonify, Blueprint
from app.utils.data_fetcher import fetch_crypto_data
from app.utils.price_predictor import predict_prices
from app.utils.signal_generator import generate_signals

bp = Blueprint('api', __name__)

@bp.route('/data')
def get_data():
    data = fetch_crypto_data()
    prediction = predict_prices()
    signals = generate_signals()
    return jsonify({
        'data': data,
        'prediction': prediction,
        'signals': signals
    })
