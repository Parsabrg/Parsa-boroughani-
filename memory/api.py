from flask import Flask, request, jsonify
import sqlite3
from memory.db import DATABASE

app = Flask(__name__)

@app.route('/ram', methods=['GET'])
def get_ram_history():
    n = int(request.args.get('n', 10))
    conn = sqlite3.connect(DATABASE)
    cursor = conn.cursor()
    cursor.execute('SELECT total, used, free, timestamp FROM ram_usage ORDER BY id DESC LIMIT ?', (n,))
    rows = cursor.fetchall()
    conn.close()

    history = [{'total': row[0], 'used': row[1], 'free': row[2], 'timestamp': row[3]} for row in rows]
    return jsonify(history)
