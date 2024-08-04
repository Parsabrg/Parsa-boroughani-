from flask import request, jsonify
from app import app
from database.db import get_ram_history

@app.route('/ram', methods=['GET'])
def ram_history():
    try:
        n = int(request.args.get('n', 10))  # Number of records as query parameter
        history = get_ram_history(n)
        return jsonify(history)
    except Exception as e:
        return jsonify({"error": str(e)})
