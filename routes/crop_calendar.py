from flask import Blueprint, render_template, request, jsonify

from services.crop_calendar_service import (
    generate_crop_calendar
)

# ==========================================
# Blueprint
# ==========================================

crop_calendar_bp = Blueprint(
    "crop_calendar",
    __name__
)

# ==========================================
# Crop Calendar Page
# ==========================================

@crop_calendar_bp.route("/crop_calendar")
def crop_calendar():

    return render_template("crop_calendar.html")


# ==========================================
# Generate AI Crop Calendar
# ==========================================

@crop_calendar_bp.route("/generate_crop_calendar", methods=["POST"])
def generate_calendar():

    try:

        data = request.get_json()

        crop = data.get("crop", "").strip()
        state = data.get("state", "").strip()

        if crop == "" or state == "":

            return jsonify({

                "error": "Please select both Crop and State."

            }), 400

        calendar = generate_crop_calendar(
            crop,
            state
        )

        return jsonify({

            "calendar": calendar

        })

    except Exception as e:

        print("Crop Calendar Route Error:", e)

        return jsonify({

            "error": "Unable to generate crop calendar."

        }), 500