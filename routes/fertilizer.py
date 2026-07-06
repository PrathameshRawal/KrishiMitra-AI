from flask import Blueprint, render_template, request, jsonify

from services.fertilizer_service import (
    generate_fertilizer_recommendation
)

# ==========================================
# Blueprint
# ==========================================

fertilizer_bp = Blueprint(
    "fertilizer",
    __name__
)

# ==========================================
# Fertilizer Page
# ==========================================

@fertilizer_bp.route("/fertilizer")
def fertilizer():

    return render_template("fertilizer.html")


# ==========================================
# AI Fertilizer Recommendation API
# ==========================================

@fertilizer_bp.route("/fertilizer-recommendation", methods=["POST"])
def fertilizer_recommendation():

    try:

        data = request.get_json()

        crop = data.get("crop", "").strip()
        soil = data.get("soil", "").strip()
        stage = data.get("stage", "").strip()

        if crop == "" or soil == "" or stage == "":

            return jsonify({

                "error": "Please fill all fields."

            }), 400

        recommendation = generate_fertilizer_recommendation(

            crop,
            soil,
            stage

        )

        return jsonify({

            "recommendation": recommendation

        })

    except Exception as e:

        print("Fertilizer Route Error:", e)

        return jsonify({

            "error": "Unable to generate fertilizer recommendation."

        }), 500