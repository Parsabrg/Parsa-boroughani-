import threading
import time
from cpu.services import (get_cpu_info)
from cpu.db import save_cpu_info
from datetime import datetime

SLEEP_TIME = 60  # Time in seconds to sleep between samples

def save_cpu_data():
    usage = get_cpu_info()
    save_cpu_info(usage, datetime.now().isoformat())

def start_saving_thread():
    def run():
        while True:
            save_cpu_data()
            time.sleep(SLEEP_TIME)

    save_thread = threading.Thread(target=run, daemon=True)
    save_thread.start()
