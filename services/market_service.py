import os
import json
import requests
from dotenv import load_dotenv
from google import genai

load_dotenv()

# ==========================================
# API Keys
# ==========================================

DATA_GOV_API_KEY = os.getenv("DATA_GOV_API_KEY")
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

RESOURCE_ID = "9ef84268-d588-465a-a308-a864a43d0070"

BASE_URL = f"https://api.data.gov.in/resource/{RESOURCE_ID}"

CACHE_FILE = "data/mandi_cache.json"

client = genai.Client(api_key=GEMINI_API_KEY)


# ==========================================
# Cache Functions
# ==========================================

def load_cache():

    try:
        with open(CACHE_FILE, "r", encoding="utf-8") as f:
            return json.load(f)

    except Exception:
        return []


def save_cache(data):

    try:

        os.makedirs("data", exist_ok=True)

        with open(CACHE_FILE, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)

    except Exception as e:
        print("Cache Save Error:", e)


# ==========================================
# Live Market Prices
# ==========================================

def get_market_prices(crop):

    params = {
        "api-key": DATA_GOV_API_KEY,
        "format": "json",
        "offset": 0,
        "limit": 20,
        "filters[commodity]": crop
    }

    try:

        response = requests.get(
            BASE_URL,
            params=params,
            timeout=15
        )

        response.raise_for_status()

        data = response.json()

        prices = []

        for item in data.get("records", []):

            prices.append({

                "crop": item.get("commodity", ""),

                "state": item.get("state", ""),

                "district": item.get("district", ""),

                "market": item.get("market", ""),

                "arrival_date": item.get("arrival_date", ""),

                "min_price": item.get("min_price", 0),

                "max_price": item.get("max_price", 0),

                "modal_price": item.get("modal_price", 0)

            })

        # Save latest successful response
        if prices:
            save_cache(prices)
            print("✅ Live market data loaded.")

        else:
            print("⚠ No live records found. Using cache.")
            prices = load_cache()

        return prices

    except Exception as e:

        print("⚠ Government API unavailable.")
        print(e)
        print("📁 Loading cached mandi prices...")

        return load_cache()


# ==========================================
# AI Market Advice
# ==========================================

def get_market_advice(crop, prices):

    if not prices:

        return (
            "No market prices are currently available. "
            "Please try again later."
        )

    summary = ""

    for p in prices[:5]:

        summary += f"""
Market : {p['market']}
State : {p['state']}
Modal Price : ₹{p['modal_price']}
"""

    prompt = f"""
You are KrishiMitra AI.

Today's mandi prices for {crop}

{summary}

Provide practical advice.

Include:

1. Should the farmer sell now?
2. Is the price good or average?
3. Should the crop be stored?
4. Which market has the best price?
5. One practical farming tip.

Keep the answer under 150 words.

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

        return (
            "Market prices are available, but AI advice "
            "could not be generated at this time."
        )