# caelum_sys/registry.py
"""
Command Registry System

This module provides the core registration system for CaelumSys commands.
All plugins use this registry to register their commands, making them
discoverable and executable by the main system.

The registry is a global dictionary that maps command phrases to their
corresponding functions. This allows for dynamic command discovery and
execution without hardcoding command lists.

Example:
    @register_command("mute volume")
    def mute_volume():
        # Command implementation
        return "Volume muted"
        
    # The command is now available via:
    # do("mute volume")
"""

# Global registry to store all registered commands
# Structure: {command_phrase: {"func": function, "safe": boolean}}
registry = {}

def register_command(trigger, safe=True):
    """
    Decorator to register a command with the CaelumSys system.
    
    This decorator allows plugin developers to easily register new commands
    that can be executed via the do() function. Commands are stored in a
    global registry with their trigger phrases and associated metadata.
    
    Args:
        trigger (str): The command phrase that triggers this function.
                      Can include placeholders like "create file at {path}"
        safe (bool): Whether this command is considered safe to execute.
                    Defaults to True. Can be used for command filtering.
    
    Returns:
        function: The decorated function, unchanged but registered.
        
    Example:
        @register_command("get current time")
        def get_time():
            return f"Current time: {datetime.now()}"
            
        @register_command("delete file at {path}", safe=False)
        def delete_file(path):
            os.remove(path)
            return f"Deleted {path}"
    """
    def wrapper(func):
        # Store the function and its metadata in the global registry
        registry[trigger.lower()] = {
            "func": func,     # The actual function to call
            "safe": safe      # Safety flag for potential filtering
        }
        return func  # Return the original function unchanged
    return wrapper

def get_registered_command(command):
    """
    Retrieve a registered command function by its trigger phrase.
    
    Args:
        command (str): The command phrase to look up (case-insensitive)
        
    Returns:
        function or None: The registered function if found, None otherwise
        
    Example:
        func = get_registered_command("mute volume")
        if func:
            result = func()
    """
    command_data = registry.get(command.lower(), {})
    return command_data.get("func", None)

def get_registered_command_phrases():
    """
    Get a list of all registered command phrases.
    
    This is useful for displaying available commands to users or for
    building help systems and documentation.
    
    Returns:
        list: A list of all registered command trigger phrases
        
    Example:
        commands = get_registered_command_phrases()
        print(f"Available commands: {len(commands)}")
        for cmd in sorted(commands):
            print(f"  • {cmd}")
    """
    return list(registry.keys())

def get_safe_registry():
    """
    Get only the commands marked as 'safe' for execution.
    
    This can be used to filter out potentially dangerous commands
    in certain contexts (e.g., when allowing external access).
    
    Returns:
        dict: Dictionary mapping safe command phrases to their functions
        
    Example:
        safe_commands = get_safe_registry()
        # Only contains commands where safe=True
    """
    return {
        command_phrase: command_data["func"]
        for command_phrase, command_data in registry.items()
        if command_data.get("safe", True)  # Default to safe if not specified
    }

def clear_registry():
    """
    Clear all registered commands from the registry.
    
    This is primarily useful for testing purposes or when you need
    to completely reset the command system.
    
    Warning:
        This will remove ALL registered commands, including built-in ones.
        Use with caution.
    """
    global registry
    registry.clear()

def get_registry_stats():
    """
    Get statistics about the current registry state.
    
    Returns:
        dict: Statistics including total commands, safe commands, etc.
        
    Example:
        stats = get_registry_stats()
        print(f"Total: {stats['total']}, Safe: {stats['safe']}")
    """
    total_commands = len(registry)
    safe_commands = len(get_safe_registry())
    
    return {
        "total": total_commands,
        "safe": safe_commands,
        "unsafe": total_commands - safe_commands
    }
