from flask import Blueprint, request, jsonify, session

from services.recommendation_service import generate_crop_recommendation

recommendation_bp = Blueprint("recommendation", __name__)


# ==========================================
# AI Crop Recommendation API
# ==========================================

@recommendation_bp.route("/recommend-crop", methods=["POST"])
def recommend_crop():

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

        state = data.get("state", "").strip()
        district = data.get("district", "").strip()
        soil = data.get("soil", "").strip()
        season = data.get("season", "").strip()
        land = data.get("land", "").strip()

        if not all([state, district, soil, season, land]):
            return jsonify({
                "error": "Please fill all fields."
            }), 400

        recommendation = generate_crop_recommendation(
            state,
            district,
            soil,
            season,
            land
        )

        return jsonify({
            "recommendation": recommendation
        })

    except Exception as e:

        print("Recommendation Error:", e)

        return jsonify({
            "error": "Unable to generate recommendation."
        }), 500