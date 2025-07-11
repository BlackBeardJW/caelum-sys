"""
Core Actions Module - Main Command Execution Engine

This module contains the heart of CaelumSys - the do() function that users
call to execute commands. It handles:

1. Plugin command discovery and execution
2. Argument parsing for parameterized commands  
3. Fallback to core system commands
4. Error handling and user feedback

The do() function is the main entry point that users interact with when
using CaelumSys. It abstracts away all the complexity of command routing,
argument parsing, and execution.

Example Usage:
    from caelum_sys import do
    
    # Simple commands (no arguments)
    result = do("mute volume")
    result = do("take screenshot")
    
    # Parameterized commands (with arguments)
    result = do("create file at test.txt")
    result = do("copy file source.txt to dest.txt")
"""

# Import the registry system for command lookup
from caelum_sys import registry
from caelum_sys.registry import get_registered_command

# Import plugin loading system
from caelum_sys.plugins import load_plugins

# Import legacy parser and executor for fallback
from .parser import parse_command
from .executor import execute

# Import libraries for advanced argument parsing
import re      # Regular expressions for pattern matching
import inspect # Function introspection for parameter analysis

# Load all plugins at startup to register their commands
# This ensures all plugin commands are available immediately
load_plugins()

def extract_arguments_from_user_input(user_input: str, command_template: str):
    """
    Extract arguments from user input based on a command template.
    
    This function handles parameterized commands like "create file at {path}"
    by matching the user's input against the template and extracting the
    values for each placeholder.
    
    Args:
        user_input (str): The actual command entered by the user
                         e.g., "create file at test.txt"
        command_template (str): The registered command pattern
                               e.g., "create file at {path}"
    
    Returns:
        dict: Mapping of placeholder names to extracted values
              e.g., {"path": "test.txt"}
              
    Example:
        args = extract_arguments_from_user_input(
            "copy file src.txt to dest.txt",
            "copy file {source} to {destination}"
        )
        # Returns: {"source": "src.txt", "destination": "dest.txt"}
    """
    # Escape special regex characters in template except for {}
    escaped_template = re.escape(command_template)
    
    # Find all placeholder names in the template
    # e.g., "create file at {path}" -> ["path"]
    placeholders = re.findall(r'\{(\w+)\}', command_template)
    
    # Replace escaped placeholders with capture groups
    # This converts the template into a regex pattern
    pattern = escaped_template
    for placeholder in placeholders:
        escaped_placeholder = re.escape(f'{{{placeholder}}}')
        # Replace each placeholder with a capture group that matches any text
        pattern = pattern.replace(escaped_placeholder, r'(.+?)')
    
    # Make the pattern match the whole string (anchored)
    pattern = f'^{pattern}$'
    
    # Try to match the user input against our pattern
    match = re.match(pattern, user_input, re.IGNORECASE)
    if match:
        # Extract the captured groups and map them to placeholder names
        args = {}
        for i, placeholder in enumerate(placeholders):
            args[placeholder] = match.group(i + 1).strip()
        return args
    
    # No match found
    return {}

def find_matching_command_template(user_input: str):
    """
    Find which registered command template matches the user input.
    
    This function searches through all registered commands to find
    parameterized commands (those with {placeholders}) that match
    the user's input pattern.
    
    Args:
        user_input (str): The command entered by the user
        
    Returns:
        tuple: (command_template, extracted_args) if match found,
               (None, {}) if no match
               
    Example:
        template, args = find_matching_command_template("create file at test.txt")
        # Returns: ("create file at {path}", {"path": "test.txt"})
    """
    # Get all registered command phrases from the registry
    registered_commands = list(registry.registry.keys())
    
    # Check each registered command to see if it matches the user input
    for command_template in registered_commands:
        # Only check parameterized commands (those with placeholders)
        if '{' in command_template:
            # Try to extract arguments using this template
            args = extract_arguments_from_user_input(user_input, command_template)
            if args:  # If we successfully extracted arguments, we found a match
                return command_template, args
    
    # No matching template found
    return None, {}

def do(command: str):
    """
    Execute a CaelumSys command and return the result.
    
    This is the main function that users call to execute any CaelumSys command.
    It handles both simple commands (like "mute volume") and parameterized 
    commands (like "create file at test.txt").
    
    The function follows this execution flow:
    1. Try to find an exact match for non-parameterized commands
    2. Try to match parameterized commands and extract arguments
    3. Fall back to legacy core commands if no plugin match found
    4. Provide user-friendly error messages for failures
    
    Args:
        command (str): The command to execute, in natural language
                      e.g., "mute volume", "create file at test.txt"
    
    Returns:
        str: Human-readable result message from the command execution
        
    Example:
        # Simple command
        result = do("get current time")
        # Returns: "⏰ Current time: 2025-07-11 15:30:45"
        
        # Parameterized command  
        result = do("create file at my_document.txt")
        # Returns: "✅ Created file at: my_document.txt"
        
    Raises:
        Various exceptions may be raised by individual commands, but the
        function attempts to catch and format them as user-friendly messages.
    """
    
    # Step 1: Try to find a direct match for non-parameterized commands
    # This handles simple commands like "mute volume", "take screenshot"
    plugin_func = get_registered_command(command)
    if plugin_func:
        try:
            # Execute the command function (no arguments needed)
            result = plugin_func()
            print(result)  # Also print for immediate feedback
            return result
        except Exception as e:
            error_msg = f"❌ Error executing '{command}': {e}"
            print(error_msg)
            return error_msg
    
    # Step 2: Try to match parameterized commands
    # This handles commands like "create file at {path}", "copy file {source} to {destination}"
    command_template, args = find_matching_command_template(command)
    if command_template:
        # Get the function associated with this command template
        plugin_func = get_registered_command(command_template)
        if plugin_func:
            try:
                # Analyze the function signature to determine how to call it
                sig = inspect.signature(plugin_func)
                param_names = list(sig.parameters.keys())
                
                # Call the function with the appropriate number of arguments
                if len(param_names) == 1:
                    # Single argument function (most common)
                    # e.g., create_file(path)
                    arg_value = list(args.values())[0]
                    result = plugin_func(arg_value)
                elif len(param_names) == 2:
                    # Two argument function (like copy, move operations)
                    # e.g., copy_file(source, destination)
                    arg_values = list(args.values())
                    result = plugin_func(arg_values[0], arg_values[1])
                else:
                    # Multiple arguments - try to match parameter names to extracted args
                    # This handles more complex function signatures
                    arg_values = [args.get(param, '') for param in param_names]
                    result = plugin_func(*arg_values)
                
                print(result)  # Print for immediate feedback
                return result
                
            except Exception as e:
                error_msg = f"❌ Error executing {command_template}: {e}"
                print(error_msg)
                return error_msg
    
    # Step 3: Fall back to legacy core commands
    # This handles older hardcoded commands for backward compatibility
    print("Current plugin registry:", registry)

    # Use the legacy parser to try to interpret the command
    intent, arg = parse_command(command)
    result = execute(intent, arg)
    print(result)
    return result

# Additional utility functions for debugging and introspection

def list_all_commands():
    """
    Get a formatted list of all available commands.
    
    Returns:
        str: Formatted string listing all commands by category
    """
    from caelum_sys.registry import get_registered_command_phrases
    
    commands = get_registered_command_phrases()
    output = f"CaelumSys - {len(commands)} Available Commands:\n"
    output += "=" * 50 + "\n"
    
    for cmd in sorted(commands):
        output += f"  • {cmd}\n"
    
    return output

def validate_command(command: str):
    """
    Check if a command is valid without executing it.
    
    Args:
        command (str): The command to validate
        
    Returns:
        dict: Validation result with details about the command
    """
    # Check for direct match
    if get_registered_command(command):
        return {
            "valid": True,
            "type": "direct",
            "command": command,
            "args": {}
        }
    
    # Check for parameterized match
    template, args = find_matching_command_template(command)
    if template:
        return {
            "valid": True,
            "type": "parameterized", 
            "template": template,
            "args": args
        }
    
    # Check legacy commands
    intent, arg = parse_command(command)
    if intent != "unknown":
        return {
            "valid": True,
            "type": "legacy",
            "intent": intent,
            "arg": arg
        }
    
    return {
        "valid": False,
        "error": "Command not recognized"
    }
