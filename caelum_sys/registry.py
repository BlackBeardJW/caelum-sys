# caelum_sys/registry.py

registry = {}

def register_command(trigger):
    """
    Decorator to register a plugin command trigger to a function.
    """
    def wrapper(func):
        registry[trigger.lower()] = func
        return func
    return wrapper

def get_registered_command(command):
    """
    Match incoming command to a registered plugin.
    """
    for trigger in registry:
        if command.lower().startswith(trigger):
            return registry[trigger]
    return None
