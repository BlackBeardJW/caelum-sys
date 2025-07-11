# caelum_sys/registry.py

registry = {}

def register_command(trigger, safe=True):
    def wrapper(func):
        registry[trigger.lower()] = {
            "func": func,
            "safe": safe
        }
        return func
    return wrapper

def get_registered_command(command):
    return registry.get(command.lower(), {}).get("func", None)

def get_registered_command_phrases():
    return list(registry.keys())

def get_safe_registry():
    return {
        k: v["func"]
        for k, v in registry.items()
        if v.get("safe", True)
    }
