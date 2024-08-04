from app import app
from database.db import init_db
from utils.threading import start_saving_thread

if __name__ == '__main__':
    init_db()
    start_saving_thread()
    app.run(debug=True)
