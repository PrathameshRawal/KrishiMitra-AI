from flask import Blueprint, request, jsonify, session
from services.gemini_service import ask_gemini
from database import get_db_connection

chatbot_bp = Blueprint("chatbot", __name__)


# =====================================
# AI Chat API
# =====================================

@chatbot_bp.route("/ask", methods=["POST"])
def ask():

    # Check login
    if "user_id" not in session:
        return jsonify({
            "reply": "Please login first."
        }), 401

    try:

        data = request.get_json()

        if not data:
            return jsonify({
                "reply": "Invalid request."
            }), 400

        question = data.get("message", "").strip()

        if question == "":
            return jsonify({
                "reply": "Please enter a question."
            }), 400

        # Gemini AI
        answer = ask_gemini(question)

        # Save Chat History
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute("""
            INSERT INTO chat_history
            (
                user_id,
                question,
                answer
            )
            VALUES
            (
                ?, ?, ?
            )
        """, (

            session["user_id"],
            question,
            answer

        ))

        conn.commit()
        conn.close()

        return jsonify({

            "reply": answer

        })

    except Exception as e:
     print("Gemini Error:", e)

    return """
Hello Farmer! 🌾

I can help you with:

• Crop recommendations
• Weather guidance
• Fertilizer suggestions
• Pest & disease management
• Government schemes
• Irrigation advice

Gemini AI is currently unavailable, so this is a demo response.
"""