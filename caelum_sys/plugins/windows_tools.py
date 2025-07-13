"""
Windows-specific tools plugin for system utilities and administrative tasks.
"""

import platform
import subprocess

from caelum_sys.registry import register_command

# Platform detection constant for all Windows-specific operations
IS_WINDOWS = platform.system() == "Windows"


def safe_windows(func):
    """Decorator to ensure commands only execute on Windows systems."""

    def wrapper(*args, **kwargs):
        if not IS_WINDOWS:
            return "❌ This command is only available on Windows."
        return func(*args, **kwargs)

    return wrapper


@register_command("open task manager")
@safe_windows
def open_task_manager():
    """Launch the Windows Task Manager."""
    subprocess.Popen("taskmgr")
    return "🧰 Task Manager opened."


@register_command("open file explorer")
@safe_windows
def open_file_explorer():
    """Launch Windows File Explorer."""
    subprocess.Popen("explorer")
    return "📁 File Explorer opened."


@register_command("lock workstation")
@safe_windows
def lock_workstation():
    """Lock the current Windows user session."""
    subprocess.Popen("rundll32.exe user32.dll,LockWorkStation")
    return "🔒 Workstation locked."


@register_command("open control panel")
@safe_windows
def open_control_panel():
    """Launch the Windows Control Panel."""
    subprocess.Popen("control")
    return "⚙️ Control Panel opened."


@register_command("open device manager")
@safe_windows
def open_device_manager():
    """Launch the Windows Device Manager console."""
    subprocess.Popen(["devmgmt.msc"])
    return "🖥️ Device Manager opened."
