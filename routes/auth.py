from flask import (
    Blueprint,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session
)

from models.user import User

auth_bp = Blueprint("auth", __name__)


# ==========================
# REGISTER
# ==========================

@auth_bp.route("/register", methods=["GET", "POST"])
def register():

    if request.method == "POST":

        full_name = request.form.get("full_name")
        email = request.form.get("email")
        mobile = request.form.get("mobile")
        password = request.form.get("password")

        state = request.form.get("state")
        district = request.form.get("district")
        village = request.form.get("village")

        land_size = request.form.get("land_size")
        soil_type = request.form.get("soil_type")
        primary_crop = request.form.get("primary_crop")
        language = request.form.get("language")

        success, message = User.create_user(
            full_name,
            email,
            mobile,
            password,
            state,
            district,
            village,
            land_size,
            soil_type,
            primary_crop,
            language
        )

        if success:
            flash("Registration Successful! Please Login.", "success")
            return redirect(url_for("auth.login"))

        flash(message, "danger")

    return render_template("register.html")


# ==========================
# LOGIN
# ==========================

@auth_bp.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        user = User.login(email, password)

        if user:

            session["user_id"] = user["id"]
            session["user_name"] = user["full_name"]

            flash("Welcome back!", "success")

            return redirect(url_for("dashboard"))

        flash("Invalid Email or Password", "danger")

    return render_template("login.html")


# ==========================
# LOGOUT
# ==========================

@auth_bp.route("/logout")
def logout():

    session.clear()

    flash("Logged out successfully.", "info")

    return redirect(url_for("auth.login"))