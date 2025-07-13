from caelum_sys.registry import register_command

@register_command("start cpu monitor")
def start_cpu_monitor():
    import threading, psutil, time

    def monitor():
        with open("cpu_log.txt", "w") as f:
            for _ in range(10):  # log 10 times over 10 seconds
                cpu = psutil.cpu_percent()
                f.write(f"CPU Usage: {cpu}%\n")
                time.sleep(1)

    threading.Thread(target=monitor, daemon=True).start()
    return "📊 CPU monitoring started (10s log in cpu_log.txt)"

@register_command("start memory monitor")
def start_memory_monitor():
    import threading, psutil, time

    def monitor():
        with open("memory_log.txt", "w") as f:
            for _ in range(10):  # log 10 times over 10 seconds
                mem = psutil.virtual_memory().percent
                f.write(f"Memory Usage: {mem}%\n")
                time.sleep(1)

    threading.Thread(target=monitor, daemon=True).start()
    return "📊 Memory monitoring started (10s log in memory_log.txt)"

@register_command("start disk monitor")
def start_disk_monitor():
    import threading, psutil, time

    def monitor():
        with open("disk_log.txt", "w") as f:
            for _ in range(10):  # log 10 times over 10 seconds
                disk = psutil.disk_usage('/').percent
                f.write(f"Disk Usage: {disk}%\n")
                time.sleep(1)

    threading.Thread(target=monitor, daemon=True).start()
    return "📊 Disk monitoring started (10s log in disk_log.txt)"