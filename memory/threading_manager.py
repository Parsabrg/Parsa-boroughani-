import threading
import time
from memory.services import get_ram_info
from memory.db import save_ram_info
from datetime import datetime

SLEEP_TIME = 60  # Time in seconds to sleep between samples

def save_ram_data():
    total, used, free = get_ram_info()
    save_ram_info(total, used, free, datetime.now().isoformat())

def start_saving_thread():
    def run():
        while True:
            save_ram_data()
            time.sleep(SLEEP_TIME)

    save_thread = threading.Thread(target=run, daemon=True)
    save_thread.start()