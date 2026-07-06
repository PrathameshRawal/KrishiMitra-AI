import os
import uuid

from flask import Blueprint, request, jsonify, session
from werkzeug.utils import secure_filename

from services.vision_service import detect_disease

disease_bp = Blueprint("disease", __name__)

UPLOAD_FOLDER = "static/uploads"

ALLOWED_EXTENSIONS = {
    "png",
    "jpg",
    "jpeg",
    "webp"
}


def allowed_file(filename):
    return (
        "." in filename
        and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS
    )


@disease_bp.route("/detect-disease", methods=["POST"])
def detect():

    # User must be logged in
    if "user_id" not in session:
        return jsonify({
            "error": "Please login first."
        }), 401

    if "image" not in request.files:
        return jsonify({
            "error": "No image uploaded."
        }), 400

    file = request.files["image"]

    if file.filename == "":
        return jsonify({
            "error": "No image selected."
        }), 400

    if not allowed_file(file.filename):
        return jsonify({
            "error": "Only JPG, JPEG, PNG and WEBP are allowed."
        }), 400

    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    extension = file.filename.rsplit(".", 1)[1].lower()

    filename = f"{uuid.uuid4()}.{extension}"

    filepath = os.path.join(
        UPLOAD_FOLDER,
        secure_filename(filename)
    )

    file.save(filepath)

    try:

        result = detect_disease(filepath)

        return jsonify(result)

    except Exception as e:

        print(e)

        return jsonify({

            "disease": "Analysis Failed",

            "confidence": "0%",

            "cause": str(e),

            "organic": "-",

            "chemical": "-",

            "prevention": "Please try again."

        }), 500