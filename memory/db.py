import sqlite3

DATABASE = 'ram_usage.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS ram_usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        total REAL,
        used REAL,
        free REAL,
        timestamp TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_ram_info(total, used, free, timestamp):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO ram_usage (total, used, free, timestamp) VALUES (?, ?, ?, ?)
    ''', (total, used, free, timestamp))
    conn.commit()
    conn.close()
