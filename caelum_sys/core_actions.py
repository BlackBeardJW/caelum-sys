from caelum_sys import registry
from caelum_sys.registry import get_registered_command
from caelum_sys.plugins import load_plugins
from .parser import parse_command
from .executor import execute
import re
import inspect

# Load all plugins at startup
load_plugins()

def extract_arguments_from_user_input(user_input: str, command_template: str):
    """
    Extract arguments from user input based on command template.
    E.g., user_input="create file at test.txt", command_template="create file at {path}"
    Returns: {"path": "test.txt"}
    """
    # Escape special regex characters in template except for {}
    escaped_template = re.escape(command_template)
    
    # Replace escaped placeholders with capture groups
    pattern = escaped_template
    placeholders = re.findall(r'\{(\w+)\}', command_template)
    
    for placeholder in placeholders:
        escaped_placeholder = re.escape(f'{{{placeholder}}}')
        pattern = pattern.replace(escaped_placeholder, r'(.+?)')
    
    # Make the pattern match the whole string
    pattern = f'^{pattern}$'
    
    match = re.match(pattern, user_input, re.IGNORECASE)
    if match:
        args = {}
        for i, placeholder in enumerate(placeholders):
            args[placeholder] = match.group(i + 1).strip()
        return args
    
    return {}

def find_matching_command_template(user_input: str):
    """
    Find which registered command template matches the user input.
    """
    registered_commands = list(registry.registry.keys())
    
    for command_template in registered_commands:
        if '{' in command_template:  # This is a parameterized command
            args = extract_arguments_from_user_input(user_input, command_template)
            if args:  # Found a match
                return command_template, args
    
    return None, {}

def do(command: str):
    # First try to find a direct match (for non-parameterized commands)
    plugin_func = get_registered_command(command)
    if plugin_func:
        result = plugin_func()
        print(result)
        return result
    
    # Try to match parameterized commands
    command_template, args = find_matching_command_template(command)
    if command_template:
        plugin_func = get_registered_command(command_template)
        if plugin_func:
            try:
                # Get function signature to determine how to call it
                sig = inspect.signature(plugin_func)
                param_names = list(sig.parameters.keys())
                
                # Call function with arguments in the correct order
                if len(param_names) == 1:
                    # Single argument function
                    arg_value = list(args.values())[0]
                    result = plugin_func(arg_value)
                elif len(param_names) == 2:
                    # Two argument function (like copy, move)
                    arg_values = list(args.values())
                    result = plugin_func(arg_values[0], arg_values[1])
                else:
                    # Try to call with all arguments in order
                    arg_values = [args.get(param, '') for param in param_names]
                    result = plugin_func(*arg_values)
                
                print(result)
                return result
            except Exception as e:
                error_msg = f"❌ Error executing {command_template}: {e}"
                print(error_msg)
                return error_msg
    
    print("Current plugin registry:", registry)

    # Fall back to core commands
    intent, arg = parse_command(command)
    result = execute(intent, arg)
    print(result)
    return result
