import psutil

def get_cpu_info():
    usage = psutil.cpu_percent(interval=1)  # CPU usage in percentage
    return usage
