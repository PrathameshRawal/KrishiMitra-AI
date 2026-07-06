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
# AI Crop Calendar
# ==========================================

def generate_crop_calendar(crop, state):

    prompt = f"""
Generate a detailed crop calendar for {crop} cultivation in {state}.

Include:
1. Land Preparation
2. Best Sowing Time
3. Irrigation Schedule
4. Fertilizer Schedule
5. Weed Management
6. Pest & Disease Management
7. Harvest Time
8. Storage Tips
9. Expected Yield
10. Best Farming Tips

Keep the response simple and farmer-friendly.
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
🌱 Land Preparation
Prepare the field well before sowing {crop} in {state}.

----------------------------------

🌾 Best Sowing Time
Use the recommended sowing season for {state}.

----------------------------------

💧 Irrigation Schedule
Provide irrigation according to crop growth stages.

----------------------------------

🧪 Fertilizer Schedule
Apply balanced NPK fertilizer and organic manure.

----------------------------------

🌿 Weed Management
Remove weeds regularly during early growth.

----------------------------------

🐛 Pest & Disease Management
Inspect crops weekly and use recommended pesticides only if necessary.

----------------------------------

✂ Harvest Time
Harvest when the crop reaches full maturity.

----------------------------------

📦 Storage Tips
Dry the produce properly before storing.

----------------------------------

💰 Expected Yield
Yield depends on soil, weather, and management practices.

----------------------------------

🌾 Best Farming Tips
• Use certified seeds.
• Follow soil testing recommendations.
• Monitor pests regularly.
• Practice proper irrigation.
"""