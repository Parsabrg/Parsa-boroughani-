import sqlite3

DATABASE = 'cpu_usage.db'

def init_db():
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS cpu_usage (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usage REAL,
        timestamp TEXT
    )
    ''')
    conn.commit()
    conn.close()

def save_cpu_info(usage, timestamp):
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('''
    INSERT INTO cpu_usage (usage, timestamp) VALUES (?, ?)
    ''', (usage, timestamp))
    conn.commit()
    conn.close()
