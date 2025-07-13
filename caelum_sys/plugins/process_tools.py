"""
Process management tools plugin for monitoring and controlling system processes.
"""

import psutil

from caelum_sys.registry import register_command


@register_command("list running processes")
def list_processes():
    """List all currently running processes."""
    processes = [proc.info["name"] for proc in psutil.process_iter(attrs=["name"])]
    return f"🧠 Running Processes:\n" + "\n".join(processes)


@register_command("kill process by name {name}", safe=False)
def kill_process_by_name(name: str):
    """Terminate processes matching the given name (UNSAFE)."""
    killed = []
    for proc in psutil.process_iter(attrs=["name"]):
        if proc.info["name"] and name.lower() in proc.info["name"].lower():
            try:
                proc.kill()
                killed.append(proc.info["name"])
            except psutil.NoSuchProcess:
                continue
    if killed:
        return f"☠️ Killed: {', '.join(killed)}"
    return f"⚠️ No process found with name matching '{name}'"


@register_command("get cpu usage")
def get_cpu_usage():
    """Get current CPU utilization percentage."""
    cpu = psutil.cpu_percent(interval=1)
    return f"💻 CPU usage: {cpu}%"


@register_command("get memory usage")
def get_memory_usage():
    """Get current system memory usage statistics."""
    mem = psutil.virtual_memory()
    return f"🧠 Memory usage: {mem.percent}% used ({mem.used // (1024 ** 2)}MB / {mem.total // (1024 ** 2)}MB)"
