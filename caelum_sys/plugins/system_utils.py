from caelum_sys.registry import register_command

import os

@register_command("lock screen", safe=False)
def lock_screen():
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "🔒 Screen locked."

@register_command("shut down in 5 minutes", safe=False)
def shutdown_timer():
    os.system("shutdown /s /t 300")
    return "⏳ System will shut down in 5 minutes."

@register_command("restart in 5 minutes", safe=False)
def restart_timer():
    os.system("shutdown /r /t 300")
    return "🔄 System will restart in 5 minutes."

@register_command("hibernate", safe=False)
def hibernate():
    os.system("shutdown /h")
    return "💤 System hibernated."

