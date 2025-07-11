import re

def parse_command(command: str):
    command = command.lower()
    if re.match(r"open (.+)", command):
        app = re.findall(r"open (.+)", command)[0]
        return ("open_app", app)
    elif "list processes" in command:
        return ("list_processes", None)
    elif re.match(r"kill (.+)", command):
        proc = re.findall(r"kill (.+)", command)[0]
        return ("kill_process", proc)
    elif "shutdown" in command:
        return ("shutdown", None)
    return ("unknown", command)
