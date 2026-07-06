from flask import Blueprint, request, jsonify

from services.market_service import (
    get_market_prices,
    get_market_advice
)

market_bp = Blueprint("market", __name__)


# ==========================================
# Live Market Prices
# ==========================================

@market_bp.route("/market-prices", methods=["POST"])
def market_prices():

    try:

        data = request.get_json()

        crop = data.get("crop", "").strip()

        if crop == "":

            return jsonify({
                "error": "Please enter a crop name."
            }), 400

        prices = get_market_prices(crop)

        if len(prices) == 0:

            return jsonify({
                "error": f"No market prices found for '{crop}'."
            }), 404

        advice = get_market_advice(crop, prices)

        return jsonify({

            "prices": prices,

            "ai_advice": advice

        })

    except Exception as e:

        print(e)

        return jsonify({

            "error": "Server Error"

        }), 500