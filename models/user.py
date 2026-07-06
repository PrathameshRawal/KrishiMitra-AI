from database import get_db_connection
from werkzeug.security import generate_password_hash, check_password_hash


class User:

    @staticmethod
    def create_user(
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
    ):

        conn = get_db_connection()
        cursor = conn.cursor()

        # Check existing email
        cursor.execute(
            "SELECT id FROM users WHERE email=?",
            (email,)
        )

        if cursor.fetchone():
            conn.close()
            return False, "Email already registered."

        hashed_password = generate_password_hash(password)

        cursor.execute("""
        INSERT INTO users(
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
        VALUES(?,?,?,?,?,?,?,?,?,?,?)
        """, (

            full_name,
            email,
            mobile,
            hashed_password,
            state,
            district,
            village,
            land_size,
            soil_type,
            primary_crop,
            language

        ))

        conn.commit()
        conn.close()

        return True, "Registration Successful"

    @staticmethod
    def login(email, password):

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE email=?",
            (email,)
        )

        user = cursor.fetchone()

        conn.close()

        if not user:
            return None

        if check_password_hash(user["password"], password):
            return user

        return None

    @staticmethod
    def get_user(user_id):

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT * FROM users WHERE id=?",
            (user_id,)
        )

        user = cursor.fetchone()

        conn.close()

        return user

    @staticmethod
    def email_exists(email):

        conn = get_db_connection()

        cursor = conn.cursor()

        cursor.execute(
            "SELECT id FROM users WHERE email=?",
            (email,)
        )

        result = cursor.fetchone()

        conn.close()

        return result is not None