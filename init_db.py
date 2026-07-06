from database import get_db_connection

conn = get_db_connection()
cursor = conn.cursor()

# =====================================================
# USERS TABLE
# =====================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    full_name TEXT NOT NULL,

    email TEXT UNIQUE NOT NULL,

    mobile TEXT NOT NULL,

    password TEXT NOT NULL,

    state TEXT,

    district TEXT,

    village TEXT,

    land_size REAL,

    soil_type TEXT,

    primary_crop TEXT,

    language TEXT DEFAULT 'English',

    profile_image TEXT DEFAULT '',

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP

)
""")

# =====================================================
# CHAT HISTORY
# =====================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    question TEXT,

    answer TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

)
""")

# =====================================================
# DISEASE HISTORY
# =====================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS disease_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    image_name TEXT,

    disease TEXT,

    confidence REAL,

    treatment TEXT,

    prevention TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

)
""")

# =====================================================
# WEATHER HISTORY
# =====================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS weather_history (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    city TEXT,

    temperature REAL,

    humidity INTEGER,

    weather TEXT,

    recommendation TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

)
""")

# =====================================================
# CROP RECOMMENDATIONS
# =====================================================
cursor.execute("""
CREATE TABLE IF NOT EXISTS recommendations (

    id INTEGER PRIMARY KEY AUTOINCREMENT,

    user_id INTEGER,

    soil TEXT,

    season TEXT,

    crop TEXT,

    recommendation TEXT,

    expected_profit TEXT,

    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY(user_id) REFERENCES users(id)

)
""")

conn.commit()
conn.close()

print("=" * 60)
print("🌱 KrishiMitra AI Database Created Successfully")
print("=" * 60)