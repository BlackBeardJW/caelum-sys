import platform
import subprocess
import psutil
import os

def open_application(app_name):
    try:
        if platform.system() == "Windows":
            subprocess.Popen(["start", "", app_name], shell=True)
        elif platform.system() == "Darwin":
            subprocess.Popen(["open", "-a", app_name])
        else:
            subprocess.Popen([app_name])
        return f"Opening {app_name}..."
    except Exception as e:
        return f"Failed to open {app_name}: {e}"

def list_processes():
    processes = [(p.pid, p.name()) for p in psutil.process_iter()]
    return "\n".join([f"{pid}: {name}" for pid, name in processes])

def kill_process(name):
    found = False
    for proc in psutil.process_iter():
        if name.lower() in proc.name().lower():
            proc.kill()
            found = True
    return f"Killed process(es) named '{name}'" if found else f"No process found named '{name}'"

def shutdown_system():
    try:
        if platform.system() == "Windows":
            os.system("shutdown /s /t 1")
        elif platform.system() == "Darwin":
            os.system("sudo shutdown -h now")
        else:
            os.system("shutdown now")
        return "System is shutting down..."
    except Exception as e:
        return f"Shutdown failed: {e}"
