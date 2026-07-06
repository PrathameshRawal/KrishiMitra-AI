from services.weather_service import get_weather
from services.market_service import get_market_prices


def get_dashboard_data():

    dashboard = {}

    # -----------------------------------
    # Weather
    # -----------------------------------

    try:

        weather = get_weather("Ichalkaranji")

        if weather:

            dashboard["weather"] = weather

        else:

            dashboard["weather"] = {

                "temperature": "--",

                "condition": "Unavailable"

            }

    except Exception:

        dashboard["weather"] = {

            "temperature": "--",

            "condition": "Unavailable"

        }

    # -----------------------------------
    # Market
    # -----------------------------------

    try:

        prices = get_market_prices("Soybean")

        if prices:

            dashboard["market"] = prices[0]

        else:

            dashboard["market"] = {

                "crop": "Soybean",

                "modal_price": "--",

                "market": "Unavailable"

            }

    except Exception:

        dashboard["market"] = {

            "crop": "Soybean",

            "modal_price": "--",

            "market": "Unavailable"

        }

    # -----------------------------------
    # Static Quick Information
    # -----------------------------------

    dashboard["recommended_crop"] = "Soybean"

    dashboard["fertilizer"] = "NPK 19:19:19"

    return dashboard