from flask import Flask, render_template, session, redirect, url_for

# Blueprints

from services.dashboard_service import get_dashboard_data
from routes.auth import auth_bp
from routes.chatbot import chatbot_bp
from routes.disease import disease_bp
from routes.weather import weather_bp
from routes.recommendation import recommendation_bp
from routes.market import market_bp
from routes.schemes import schemes_bp
from routes.fertilizer import fertilizer_bp
from routes.crop_calendar import crop_calendar_bp
from routes.voice import voice_bp

# -------------------------
# Flask App
# -------------------------

app = Flask(__name__)

app.secret_key = "krishmitra_super_secret_key"

# -------------------------
# Register Blueprints
# -------------------------

app.register_blueprint(auth_bp)
app.register_blueprint(chatbot_bp)
app.register_blueprint(disease_bp)
app.register_blueprint(weather_bp)
app.register_blueprint(recommendation_bp)
app.register_blueprint(market_bp)
app.register_blueprint(schemes_bp)
app.register_blueprint(fertilizer_bp)
app.register_blueprint(crop_calendar_bp)
app.register_blueprint(voice_bp)

# -------------------------
# Routes
# -------------------------

@app.route("/")
def home():
    return render_template("index.html")


@app.route("/dashboard")
def dashboard():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    dashboard_data = get_dashboard_data()

    return render_template(
        "dashboard.html",
        user_name=session.get("user_name"),
        dashboard=dashboard_data
    )


@app.route("/chatbot")
def chatbot():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("chatbot.html")


@app.route("/weather")
def weather():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("weather.html")


@app.route("/disease")
def disease():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("disease.html")


@app.route("/recommendation")
def recommendation():

    if "user_id" not in session:
        return redirect(url_for("auth.login"))

    return render_template("recommendation.html")


@app.route("/market")
def market():
    return render_template("market.html")


# -------------------------
# Custom 404 Page
# -------------------------

@app.errorhandler(404)
def page_not_found(error):

    return render_template("404.html"), 404


if __name__ == "__main__":
    app.run(debug=True)