from flask import Blueprint, render_template, request, jsonify
from google import genai
from dotenv import load_dotenv
from services.weather_service import get_weather_with_advice
import os
import re

load_dotenv()

# ==========================================
# Gemini Configuration
# ==========================================

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)

# ==========================================
# Blueprint
# ==========================================

voice_bp = Blueprint(
    "voice",
    __name__
)

# ==========================================
# Voice Assistant Page
# ==========================================

@voice_bp.route("/voice")
def voice():

    return render_template("voice.html")


# ==========================================
# Voice Chat API
# ==========================================

@voice_bp.route("/voice-chat", methods=["POST"])
def voice_chat():

    try:

        data = request.get_json()

        question = data.get("question", "").strip()

        language = data.get("language", "en-IN")

        if question == "":

            return jsonify({
                "error": "Please ask a question."
            }), 400

        # ==========================================
        # Reply Language
        # ==========================================

        if language == "hi-IN":

            reply_language = "Hindi"

        elif language == "mr-IN":

            reply_language = "Marathi"

        else:

            reply_language = "English"

        question_lower = question.lower()

        # ==========================================
        # WEATHER MODULE
        # ==========================================

        if (
            "weather" in question_lower
            or "rain" in question_lower
            or "temperature" in question_lower
            or "मौसम" in question
            or "बारिश" in question
            or "हवामान" in question
            or "पाऊस" in question
        ):

            city = "Ichalkaranji"

            match = re.search(
                r"in\s+([A-Za-z ]+)",
                question,
                re.IGNORECASE
            )

            if match:

                city = match.group(1).strip()

            weather = get_weather_with_advice(city)

            if weather is None:

                return jsonify({

                    "answer": f"Unable to fetch weather for {city}."

                })

            if reply_language == "Hindi":

                answer = f"""
🌤 {weather['city']} का मौसम

🌡 तापमान : {weather['temperature']}°C
☁ मौसम : {weather['condition']}
💧 आर्द्रता : {weather['humidity']}%
🌧 बारिश : {weather['rain']}
🌦 वर्षा संभावना : {weather['rain_probability']}
🌧 वर्षा : {weather['rainfall']}
💨 हवा : {weather['wind']} km/h

🌾 कृषि सलाह

{weather['ai_advice']}
"""

            elif reply_language == "Marathi":

                answer = f"""
🌤 {weather['city']} चे हवामान

🌡 तापमान : {weather['temperature']}°C
☁ हवामान : {weather['condition']}
💧 आर्द्रता : {weather['humidity']}%
🌧 पाऊस : {weather['rain']}
🌦 पावसाची शक्यता : {weather['rain_probability']}
🌧 पर्जन्यमान : {weather['rainfall']}
💨 वारा : {weather['wind']} km/h

🌾 शेती सल्ला

{weather['ai_advice']}
"""

            else:

                answer = f"""
🌤 Weather in {weather['city']}

🌡 Temperature : {weather['temperature']}°C
☁ Condition : {weather['condition']}
💧 Humidity : {weather['humidity']}%
🌧 Rain : {weather['rain']}
🌦 Rain Probability : {weather['rain_probability']}
🌧 Rainfall : {weather['rainfall']}
💨 Wind : {weather['wind']} km/h

🌾 Farming Advice

{weather['ai_advice']}
"""

            return jsonify({

                "answer": answer

            })

        # ==========================================
        # GEMINI FOR ALL OTHER QUESTIONS
        # ==========================================

        prompt = f"""
You are KrishiMitra AI.

You are an expert Indian Agriculture Assistant.

Answer ONLY in {reply_language}.

Farmer Question:

{question}

Rules:

• Use simple language.
• Give practical farming advice.
• Keep answer below 150 words.
"""

        response = client.models.generate_content(

            model="gemini-2.5-flash",

            contents=prompt

        )

        return jsonify({

            "answer": response.text

        })

    except Exception as e:

        print("Voice Error:", e)

        return jsonify({

            "error": "Unable to process your request."

        }), 500