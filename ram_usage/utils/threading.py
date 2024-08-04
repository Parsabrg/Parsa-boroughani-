import threading
import time
from database.db import save_ram_info
from config import SLEEP_TIME

def start_saving_thread():
    def run():
        while True:
            save_ram_info()
            time.sleep(SLEEP_TIME)  # Read sleep time from config

    save_thread = threading.Thread(target=run, daemon=True)
    save_thread.start()
