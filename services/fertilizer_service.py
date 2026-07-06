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
# AI Fertilizer Recommendation
# ==========================================

def generate_fertilizer_recommendation(crop, soil, stage):

    prompt = f"""
You are KrishiMitra AI, an experienced Indian Agriculture Expert.

Farmer Details:

Crop: {crop}
Soil Type: {soil}
Growth Stage: {stage}

Generate a fertilizer recommendation in the following format.

🌱 Recommended Fertilizer
Mention the best fertilizer.

----------------------------------

🧪 Recommended NPK Ratio

Mention suitable NPK ratio.

----------------------------------

🌿 Organic Alternatives

Suggest organic manure or compost.

----------------------------------

💧 Application Method

Explain how to apply fertilizer.

----------------------------------

📅 Best Time to Apply

Mention the best time of day and crop stage.

----------------------------------

⚠ Precautions

Give 4 important precautions.

----------------------------------

💰 Cost Saving Tips

Give 3 practical tips.

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

        return """
Unable to generate fertilizer recommendation.

Please try again later.
"""