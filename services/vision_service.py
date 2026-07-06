import os
import json
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(
    api_key=os.getenv("GEMINI_API_KEY")
)


PROMPT = """
You are an expert agricultural scientist.

Analyze the uploaded crop or leaf image carefully.

Return ONLY valid JSON.

Format:

{
  "disease":"...",
  "confidence":"...",
  "cause":"...",
  "organic":"...",
  "chemical":"...",
  "prevention":"..."
}

Rules:

- If healthy, disease = "Healthy Plant"
- Confidence should be like 96%
- Organic treatment should be practical.
- Chemical treatment should mention common fungicide/insecticide if needed.
- Prevention should be short and practical.
- Never return markdown.
- Never use ```json.
- Return ONLY JSON.
"""


def detect_disease(image_path):

    try:

        uploaded_file = client.files.upload(
            file=image_path
        )

        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=[
                uploaded_file,
                PROMPT
            ]
        )

        text = response.text.strip()

        if text.startswith("```"):
            text = text.replace("```json", "")
            text = text.replace("```", "").strip()

        return json.loads(text)

    except Exception as e:

     print("Gemini Error:", e)

    if "RESOURCE_EXHAUSTED" in str(e):

        return {

            "disease": "Demo Mode",

            "confidence": "95%",

            "cause": "Gemini API quota exceeded.",

            "organic": "Spray Neem Oil every 7 days.",

            "chemical": "Use recommended fungicide if infection spreads.",

            "prevention": "Inspect crops weekly and use disease-resistant seeds."

        }

    return {

        "disease": "Unable to detect",

        "confidence": "0%",

        "cause": str(e),

        "organic": "-",

        "chemical": "-",

        "prevention": "Please upload a clearer image."

    }