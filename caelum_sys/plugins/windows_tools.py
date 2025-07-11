from caelum_sys.registry import register_command
import platform
import subprocess

IS_WINDOWS = platform.system() == "Windows"

def safe_windows(func):
    def wrapper(*args, **kwargs):
        if not IS_WINDOWS:
            return "❌ This command is only available on Windows."
        return func(*args, **kwargs)
    return wrapper

@register_command("open task manager")
@safe_windows
def open_task_manager():
    subprocess.Popen("taskmgr")
    return "🧰 Task Manager opened."

@register_command("open file explorer")
@safe_windows
def open_file_explorer():
    subprocess.Popen("explorer")
    return "📁 File Explorer opened."

@register_command("lock workstation")
@safe_windows
def lock_workstation():
    subprocess.Popen("rundll32.exe user32.dll,LockWorkStation")
    return "🔒 Workstation locked."

@register_command("open control panel")
@safe_windows
def open_control_panel():
    subprocess.Popen("control")
    return "⚙️ Control Panel opened."

@register_command("open device manager")
@safe_windows
def open_device_manager():
    subprocess.Popen(["devmgmt.msc"])
    return "🖥️ Device Manager opened."
