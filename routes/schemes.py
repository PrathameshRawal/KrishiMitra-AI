from flask import Blueprint, render_template, request, jsonify

from services.scheme_service import (
    get_schemes,
    generate_scheme_advice
)

# ==========================================
# Blueprint
# ==========================================

schemes_bp = Blueprint(
    "schemes",
    __name__
)

# ==========================================
# Schemes Page
# ==========================================

@schemes_bp.route("/schemes")
def schemes():

    return render_template("schemes.html")


# ==========================================
# Get Government Schemes
# ==========================================

@schemes_bp.route("/get-schemes", methods=["POST"])
def get_scheme_data():

    try:

        data = request.get_json()

        state = data.get("state", "").strip()

        category = data.get("category", "").strip()

        if state == "" or category == "":

            return jsonify({

                "error": "Please select State and Farmer Category."

            }), 400

        # Fetch schemes
        schemes = get_schemes(state, category)

        # Generate AI explanation
        ai_advice = generate_scheme_advice(
            state,
            category,
            schemes
        )

        return jsonify({

            "schemes": schemes,

            "ai_advice": ai_advice

        })

    except Exception as e:

        print("Schemes Route Error:", e)

        return jsonify({

            "error": "Unable to fetch government schemes."

        }), 500