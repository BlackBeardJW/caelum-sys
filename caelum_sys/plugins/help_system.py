"""Help and discovery plugin for listing available commands."""

from caelum_sys.registry import register_command, registry


@register_command("help", safe=True)
def show_help():
    """Show all available commands organized by category."""
    try:
        plugins = {}
        for cmd_phrase, cmd_data in registry.items():
            func = cmd_data['func']
            module_name = func.__module__.split('.')[-1]
            
            if module_name not in plugins:
                plugins[module_name] = []
            plugins[module_name].append(cmd_phrase)
        
        output = f"🚀 CaelumSys v0.3.0 - {len(registry)} Available Commands (Early Development)\n"
        output += "=" * 50 + "\n\n"
        
        for plugin_name, commands in sorted(plugins.items()):
            display_name = plugin_name.replace('_', ' ').title()
            output += f"📦 {display_name} ({len(commands)} commands):\n"
            for cmd in sorted(commands):
                output += f"   • {cmd}\n"
            output += "\n"
        
        output += "💡 Usage: do('command') or caelum-sys command\n"
        output += "⚠️ Early development - APIs may change between versions\n"
        output += "🔒 Safe commands prepared for future LLM agent integration"
        
        return output
    except Exception as e:
        return f"❌ Error showing help: {e}"

@register_command("list safe commands", safe=True)  
def list_safe_commands():
    """Show only commands marked as safe for LLM use."""
    try:
        safe_commands = [cmd for cmd, data in registry.items() if data.get('safe', True)]
        output = f"✅ Safe Commands ({len(safe_commands)} total):\n"
        output += "=" * 40 + "\n"
        
        for cmd in sorted(safe_commands):
            output += f"   • {cmd}\n"
            
        return output
    except Exception as e:
        return f"❌ Error listing safe commands: {e}"

@register_command("list unsafe commands", safe=True)
def list_unsafe_commands():
    """Show commands that require permission for safety."""
    try:
        unsafe_commands = [cmd for cmd, data in registry.items() if not data.get('safe', True)]
        output = f"⚠️ Unsafe Commands ({len(unsafe_commands)} total):\n"
        output += "=" * 40 + "\n"
        
        for cmd in sorted(unsafe_commands):
            output += f"   • {cmd}\n"
            
        output += "\n💡 These commands modify system state and need explicit permission"
        return output
    except Exception as e:
        return f"❌ Error listing unsafe commands: {e}"

@register_command("search commands for {keyword}", safe=True)
def search_commands(keyword: str):
    """Search for commands containing specific keywords."""
    try:
        matching_commands = [cmd for cmd in registry.keys() if keyword.lower() in cmd.lower()]
        
        if not matching_commands:
            return f"🔍 No commands found containing '{keyword}'"
        
        output = f"🔍 Commands containing '{keyword}' ({len(matching_commands)} found):\n"
        output += "=" * 40 + "\n"
        
        for cmd in sorted(matching_commands):
            safety = "✅" if registry[cmd].get('safe', True) else "⚠️"
            output += f"   {safety} {cmd}\n"
            
        return output
    except Exception as e:
        return f"❌ Error searching commands: {e}"
