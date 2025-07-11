from caelum_sys.registry import register_command
import datetime
import platform

@register_command("get current time")
def get_time():
    now = datetime.datetime.now()
    return f"⏰ Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

@register_command("get system info")
def get_system_info():
    info = platform.uname()
    return f"🖥️ System Info:\n" \
           f"System: {info.system}\n" \
           f"Node: {info.node}\n" \
           f"Release: {info.release}\n" \
           f"Version: {info.version}\n" \
           f"Machine: {info.machine}\n" \
           f"Processor: {info.processor}"

@register_command("say hello")
def say_hello():
    return "👋 Hello from Caelum-Sys!"

@register_command("get python version")
def get_python_version():
    return f"🐍 Python Version: {platform.python_version()}"
