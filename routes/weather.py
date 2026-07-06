from flask import Blueprint, request, jsonify, session

from services.weather_service import get_weather_with_advice

weather_bp = Blueprint("weather", __name__)


# ======================================
# Weather API
# ======================================

@weather_bp.route("/weather-data", methods=["POST"])
def weather_data():

    # User must be logged in
    if "user_id" not in session:

        return jsonify({

            "error": "Please login first."

        }), 401

    try:

        data = request.get_json()

        if not data:

            return jsonify({

                "error": "Invalid request."

            }), 400

        city = data.get("city", "").strip()

        if city == "":

            return jsonify({

                "error": "Please enter a city."

            }), 400

        weather = get_weather_with_advice(city)

        if weather is None:

            return jsonify({

                "error": "City not found."

            }), 404

        return jsonify(weather)

    except Exception as e:

        print(e)

        return jsonify({

            "error": "Unable to fetch weather."

        }), 500