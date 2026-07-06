import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ==========================================
# Gemini Configuration
# ==========================================

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

client = genai.Client(
    api_key=GEMINI_API_KEY
)

# ==========================================
# AI Crop Recommendation
# ==========================================

def generate_crop_recommendation(state, district, soil, season, land):

    prompt = f"""
You are KrishiMitra AI, an experienced agricultural expert helping Indian farmers.

Farmer Details:

State: {state}
District: {district}
Soil Type: {soil}
Season: {season}
Land Size: {land} Acres

Analyze the farm conditions and provide recommendations.

Return ONLY in the following format.

🌾 BEST CROPS

🥇 Crop 1
Reason

🥈 Crop 2
Reason

🥉 Crop 3
Reason

----------------------------------

📈 Expected Yield

Mention approximate yield.

----------------------------------

💰 Estimated Profit

Mention approximate income.

----------------------------------

🧪 Fertilizer

Mention NPK or organic fertilizer.

----------------------------------

💧 Irrigation

Mention irrigation schedule.

----------------------------------

📅 Best Sowing Time

----------------------------------

🌾 Harvest Time

----------------------------------

⚠ Risks

Mention possible diseases or weather risks.

----------------------------------

🌱 Sustainable Farming Tips

Give 4 practical tips.

Keep the answer under 250 words.

Use simple English.
"""

    try:

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
        )

        return response.text

    except Exception as e:

     print("Gemini Error:", e)

    return f"""
🌾 BEST CROPS

🥇 Rice
Suitable for {soil} soil during the {season} season in {state}.

🥈 Maize
Good market demand with moderate irrigation requirements.

🥉 Soybean
Provides good returns and improves soil fertility.

----------------------------------

📈 Expected Yield

20–30 Quintals per Acre

----------------------------------

💰 Estimated Profit

₹40,000 – ₹70,000 per Acre

----------------------------------

🧪 Fertilizer

Apply NPK (120:60:40) along with organic compost.

----------------------------------

💧 Irrigation

Provide irrigation every 7–10 days depending on rainfall.

----------------------------------

📅 Best Sowing Time

Start sowing at the beginning of the {season} season.

----------------------------------

🌾 Harvest Time

Harvest after 100–120 days depending on the crop.

----------------------------------

⚠ Risks

Monitor for pest attacks, fungal diseases, and irregular rainfall.

----------------------------------

🌱 Sustainable Farming Tips

• Use certified quality seeds.
• Test soil before fertilizer application.
• Practice crop rotation.
• Use drip irrigation to save water.
"""