from memory.api import app
from memory.threading_manager import start_saving_thread as start_ram_thread
from memory.db import init_db as init_ram_db
from cpu.threading_manager import start_saving_thread as start_cpu_thread
from cpu.db import init_db as init_cpu_db

if name == 'main':
    init_ram_db()
    init_cpu_db()

    start_ram_thread()
    start_cpu_thread()

    app.run(debug=True)
