import sqlite3

# ==========================================
# DATABASE CONNECTION
# ==========================================

conn = sqlite3.connect(
    "aiva_memory.db",
    check_same_thread=False
)

cursor = conn.cursor()

# ==========================================
# CREATE TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS chat_history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    role TEXT,
    message TEXT
)
""")

conn.commit()

# ==========================================
# SAVE MESSAGE
# ==========================================

def save_message(role, message):

    cursor.execute(
        "INSERT INTO chat_history(role, message) VALUES (?, ?)",
        (role, message)
    )

    conn.commit()

# ==========================================
# LOAD MESSAGES
# ==========================================

def load_messages():

    cursor.execute(
        "SELECT role, message FROM chat_history"
    )

    rows = cursor.fetchall()

    return [
        {
            "role": row[0],
            "content": row[1]
        }
        for row in rows
    ]

# ==========================================
# CLEAR MEMORY
# ==========================================

def clear_memory():

    cursor.execute(
        "DELETE FROM chat_history"
    )

    conn.commit()