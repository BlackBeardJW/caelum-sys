from caelum_sys.registry import register_command
import psutil

@register_command("get cpu usage")
def cpu_usage(command: str):
    return f"🧠 CPU Usage: {psutil.cpu_percent()}%"

@register_command("get memory stats")
def memory_stats(command: str):
    mem = psutil.virtual_memory()
    return f"💾 Memory: {mem.used // (1024**2)}MB used / {mem.total // (1024**2)}MB total ({mem.percent}%)"
