import psutil

def get_ram_info():
    ram = psutil.virtual_memory()
    total = ram.total / (1024 ** 2)  # Convert to MB
    used = ram.used / (1024 ** 2)    # Convert to MB
    free = ram.free / (1024 ** 2)    # Convert to MB
    return total, used, free
