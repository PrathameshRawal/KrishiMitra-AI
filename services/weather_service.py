import os
from datetime import datetime

import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

# -------------------------------------------------
# API Keys
# -------------------------------------------------

OPENWEATHER_API_KEY = os.getenv("OPENWEATHER_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# -------------------------------------------------
# Get Weather
# -------------------------------------------------

def get_weather(city):

    url = "https://api.openweathermap.org/data/2.5/forecast"

    params = {
        "q": city,
        "appid": OPENWEATHER_API_KEY,
        "units": "metric"
    }

    response = requests.get(url, params=params)

    if response.status_code != 200:
        return None

    forecast = response.json()

    item = forecast["list"][0]
    city_info = forecast["city"]

    rainfall = item.get("rain", {}).get("3h", 0)

    return {

        "city": city_info["name"],

        "temperature": round(item["main"]["temp"]),

        "feels_like": round(item["main"]["feels_like"]),

        "humidity": item["main"]["humidity"],

        "wind": round(item["wind"]["speed"] * 3.6),

        "condition": item["weather"][0]["description"].title(),

        "rain": "Yes" if item["pop"] > 0.3 else "No",

        "rainfall": f"{rainfall} mm",

        "rain_probability": f"{int(item['pop'] * 100)}%",

        "visibility": f"{item['visibility'] / 1000:.1f} km",

        "sunrise": datetime.fromtimestamp(
            city_info["sunrise"]
        ).strftime("%I:%M %p"),

        "sunset": datetime.fromtimestamp(
            city_info["sunset"]
        ).strftime("%I:%M %p")

    }


# -------------------------------------------------
# Gemini Farming Advice
# -------------------------------------------------

def get_ai_advice(weather):

    prompt = f"""
You are KrishiMitra AI.

Weather Details:

City: {weather['city']}

Temperature: {weather['temperature']}°C

Condition: {weather['condition']}

Humidity: {weather['humidity']}%

Wind: {weather['wind']} km/h

Rain Probability: {weather['rain_probability']}

Rainfall: {weather['rainfall']}

Visibility: {weather['visibility']}

Give practical farming advice.

Rules:

- Use simple language.
- Maximum 6 bullet points.
- Mention irrigation.
- Mention pesticide spraying.
- Mention fertilizer.
- Mention sowing.
- Mention disease risk.
- Mention weather precautions.
- Keep the answer under 150 words.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception:

        return """
• Check your crop regularly.

• Irrigate only if soil is dry.

• Avoid spraying pesticides during rain.

• Apply fertilizer as recommended.

• Protect crops from heavy wind and rainfall.

• Monitor crops for fungal diseases.
"""


# -------------------------------------------------
# Combined Function
# -------------------------------------------------

def get_weather_with_advice(city):

    weather = get_weather(city)

    if weather is None:
        return None

    weather["ai_advice"] = get_ai_advice(weather)

    return weather