"""Core Actions Module - Main Command Execution Engine"""

import inspect
import re

from caelum_sys import registry
from caelum_sys.registry import get_registered_command


def extract_arguments_from_user_input(user_input: str, command_template: str):
    """Extract argument values from user input based on command template."""
    escaped_template = re.escape(command_template)
    placeholders = re.findall(r"\{(\w+)\}", command_template)

    pattern = escaped_template
    for placeholder in placeholders:
        escaped_placeholder = re.escape(f"{{{placeholder}}}")
        pattern = pattern.replace(escaped_placeholder, r"(.+?)")

    pattern = f"^{pattern}$"
    match = re.match(pattern, user_input, re.IGNORECASE)
    if match:
        args = {}
        for i, placeholder in enumerate(placeholders):
            args[placeholder] = match.group(i + 1).strip()
        return args

    return {}


def find_matching_command_template(user_input: str):
    """Find which registered command template matches the user input."""
    registered_commands = list(registry.registry.keys())

    for command_template in registered_commands:
        if "{" in command_template:
            args = extract_arguments_from_user_input(user_input, command_template)
            if args:
                return command_template, args

    return None, {}


def do(command: str):
    """Execute a CaelumSys command and return the result."""

    # Try direct match for simple commands
    plugin_func = get_registered_command(command)
    if plugin_func:
        try:
            result = plugin_func()
            return result
        except Exception as e:
            return f"❌ Error executing '{command}': {e}"

    # Try parameterized commands
    command_template, args = find_matching_command_template(command)
    if command_template:
        plugin_func = get_registered_command(command_template)
        if plugin_func:
            try:
                sig = inspect.signature(plugin_func)
                param_names = list(sig.parameters.keys())

                if len(param_names) == 1:
                    arg_value = list(args.values())[0]
                    result = plugin_func(arg_value)
                elif len(param_names) == 2:
                    arg_values = list(args.values())
                    result = plugin_func(arg_values[0], arg_values[1])
                else:
                    arg_values = [args.get(param, "") for param in param_names]
                    result = plugin_func(*arg_values)

                return result

            except Exception as e:
                return f"❌ Error executing {command_template}: {e}"

    return f"Unknown command: {command}"


def list_all_commands():
    """Get a formatted list of all available commands."""
    from caelum_sys.registry import get_registered_command_phrases

    commands = get_registered_command_phrases()
    output = f"CaelumSys - {len(commands)} Available Commands:\n"
    output += "=" * 50 + "\n"

    for cmd in sorted(commands):
        output += f"  • {cmd}\n"

    return output


def validate_command(command: str):
    """Check if a command is valid without executing it."""
    # Check for direct match
    if get_registered_command(command):
        return {"valid": True, "type": "direct", "command": command, "args": {}}

    # Check for parameterized match
    template, args = find_matching_command_template(command)
    if template:
        return {
            "valid": True,
            "type": "parameterized",
            "template": template,
            "args": args,
        }

    return {"valid": False, "error": "Command not recognized"}
