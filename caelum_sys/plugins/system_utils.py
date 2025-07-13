"""
System utilities plugin for power management and screen locking operations.
"""

from caelum_sys.registry import register_command
import os  # For executing system-level commands

@register_command("lock screen", safe=False)
def lock_screen():
    """Lock the current Windows workstation."""
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "🔒 Screen locked."

@register_command("shut down in 5 minutes", safe=False)
def shutdown_timer():
    """Schedule a system shutdown in 5 minutes."""
    os.system("shutdown /s /t 300")
    return "⏳ System will shut down in 5 minutes."

@register_command("restart in 5 minutes", safe=False)
def restart_timer():
    """Schedule a system restart in 5 minutes."""
    os.system("shutdown /r /t 300")
    return "🔄 System will restart in 5 minutes."

@register_command("hibernate", safe=False)
def hibernate():
    """Put the system into hibernation mode."""
    os.system("shutdown /h")
    return "💤 System hibernated."

# Utility functions for system power management

def _cancel_scheduled_shutdown():
    """Cancel any pending shutdown or restart."""
    try:
        result = os.system("shutdown /a")
        if result == 0:
            return "✅ Scheduled shutdown/restart cancelled"
        else:
            return "❌ No shutdown was scheduled or cancellation failed"
    except Exception as e:
        return f"❌ Error cancelling shutdown: {e}"

def _check_hibernation_support():
    """Check if hibernation is supported on this system."""
    return True  # Assume supported for now

@register_command("clear temp files", safe=False)
def clear_temp_files():
    """Clear temporary files from the system."""
    import os
    import shutil
    temp_path = os.environ.get("TEMP", None)
    if not temp_path:
        return "❌ TEMP directory not found."

    deleted = 0
    for filename in os.listdir(temp_path):
        path = os.path.join(temp_path, filename)
        try:
            if os.path.isfile(path):
                os.remove(path)
                deleted += 1
            elif os.path.isdir(path):
                shutil.rmtree(path, ignore_errors=True)
                deleted += 1
        except:
            continue
    return f"🧹 Cleared {deleted} temp files/folders."


