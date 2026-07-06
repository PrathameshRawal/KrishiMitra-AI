import sqlite3
import os

# Database folder
DB_FOLDER = "database"
DB_NAME = "krishmitra.db"

# Create database folder if it doesn't exist
if not os.path.exists(DB_FOLDER):
    os.makedirs(DB_FOLDER)

DATABASE_PATH = os.path.join(DB_FOLDER, DB_NAME)


def get_db_connection():
    """
    Returns SQLite database connection.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    return conn