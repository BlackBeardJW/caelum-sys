from caelum_sys.registry import get_registered_command_phrases, register_command


@register_command("list available commands")
def list_available_commands():
    cmds = sorted(get_registered_command_phrases())
    return "🧠 Available commands:\n" + "\n".join(f"- {c}" for c in cmds)
