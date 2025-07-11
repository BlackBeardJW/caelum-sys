from caelum_sys import registry
from caelum_sys.registry import get_registered_command
from caelum_sys.plugins import load_plugins
from .parser import parse_command
from .executor import execute

# Load all plugins at startup
load_plugins()

def do(command: str):
    # Try plugin commands first
    plugin_func = get_registered_command(command)
    if plugin_func:
        result = plugin_func(command)
        print(result)
        return result
    print("Current plugin registry:", registry)

    # Fall back to core commands
    intent, arg = parse_command(command)
    result = execute(intent, arg)
    print(result)
    return result
