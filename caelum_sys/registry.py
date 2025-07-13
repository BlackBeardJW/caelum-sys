"""Command Registry System for CaelumSys"""

# Global registry to store all registered commands
registry = {}


def register_command(trigger, safe=True):
    """Decorator to register a command with the CaelumSys system.
    
    Args:
        trigger: The command phrase that triggers this function
        safe: Whether this command is safe to execute (default: True)
    """
    def wrapper(func):
        registry[trigger.lower()] = {
            "func": func,
            "safe": safe
        }
        return func
    return wrapper


def get_registered_command(command):
    """Retrieve a registered command function by its trigger phrase."""
    command_data = registry.get(command.lower(), {})
    return command_data.get("func", None)


def get_registered_command_phrases():
    """Get a list of all registered command phrases."""
    return list(registry.keys())


def get_safe_registry():
    """Get only the commands marked as 'safe' for execution."""
    return {
        command_phrase: command_data["func"]
        for command_phrase, command_data in registry.items()
        if command_data.get("safe", True)
    }

def clear_registry():
    """Clear all registered commands from the registry (mainly for testing)."""
    global registry
    registry.clear()


def get_registry_stats():
    """Get statistics about the current registry state."""
    total_commands = len(registry)
    safe_commands = len(get_safe_registry())
    
    return {
        "total": total_commands,
        "safe": safe_commands,
        "unsafe": total_commands - safe_commands
    }
