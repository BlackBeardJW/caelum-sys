from . import system
from .parser import parse_command

def execute(intent, arg):
    if intent == "open_app":
        return system.open_application(arg)
    elif intent == "list_processes":
        return system.list_processes()
    elif intent == "kill_process":
        return system.kill_process(arg)
    elif intent == "shutdown":
        return system.shutdown_system()
    else:
        return f"Unknown command: {arg}"
