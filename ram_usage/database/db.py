import sqlite3
from datetime import datetime
from app.ram_info import get_ram_info
from config import DATABASE

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

def save_ram_info():
    try:
        total, used, free = get_ram_info()
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('''
        INSERT INTO ram_usage (total, used, free, timestamp) VALUES (?, ?, ?, ?)
        ''', (total, used, free, datetime.now().isoformat()))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving RAM info: {e}")

def get_ram_history(n):
    try:
        conn = sqlite3.connect(DATABASE)
        cursor = conn.cursor()
        cursor.execute('SELECT total, used, free, timestamp FROM ram_usage ORDER BY id DESC LIMIT ?', (n,))
        rows = cursor.fetchall()
        conn.close()
        
        history = [{'total': row[0], 'used': row[1], 'free': row[2], 'timestamp': row[3]} for row in rows]
        return history
    except Exception as e:
        raise e
