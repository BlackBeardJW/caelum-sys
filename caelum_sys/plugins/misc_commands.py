"""
Miscellaneous commands plugin for time, system info, and basic utilities.
"""

import datetime
import platform

from caelum_sys.registry import register_command


@register_command("get current time")
def get_time():
    """Get the current date and time."""
    now = datetime.datetime.now()
    return f"⏰ Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"


@register_command("get system info")
def get_system_info():
    """Get detailed system platform information."""
    info = platform.uname()
    return (
        f"🖥️ System Info:\n"
        f"System: {info.system}\n"
        f"Node: {info.node}\n"
        f"Release: {info.release}\n"
        f"Version: {info.version}\n"
        f"Machine: {info.machine}\n"
        f"Processor: {info.processor}"
    )


@register_command("say hello")
def say_hello():
    """Simple greeting message."""
    return "👋 Hello from Caelum-Sys!"


@register_command("get python version")
def get_python_version():
    """Get the Python interpreter version."""
    return f"🐍 Python Version: {platform.python_version()}"
