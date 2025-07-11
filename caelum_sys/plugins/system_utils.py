"""
System Utilities Plugin

This plugin provides system-level operations like locking the screen,
shutting down, restarting, and hibernating the computer. These commands
are marked as 'safe=False' because they can significantly impact the
system state.

Commands provided:
- "lock screen" - Lock the workstation
- "shut down in 5 minutes" - Schedule system shutdown
- "restart in 5 minutes" - Schedule system restart  
- "hibernate" - Put system into hibernation

Dependencies:
- os: For executing system commands

Safety Notes:
- All commands in this plugin are marked as safe=False
- Shutdown/restart commands use a 5-minute delay for safety
- These operations may cause data loss if unsaved work exists
- Hibernate may not work on all systems depending on configuration

Platform:
- Windows-specific commands using Windows system utilities
"""

from caelum_sys.registry import register_command
import os  # For executing system-level commands

@register_command("lock screen", safe=False)
def lock_screen():
    """
    Lock the current Windows workstation.
    
    This command immediately locks the screen, requiring the user to
    re-enter their password to access the system. This is useful for
    quickly securing the computer when stepping away.
    
    Returns:
        str: Success message indicating the screen was locked
        
    Example:
        result = do("lock screen")
        # Result: "🔒 Screen locked."
        # (Screen immediately locks)
        
    Note:
        This command is marked as safe=False because it changes the
        system state by locking the user session.
    """
    # Use Windows API to lock the workstation
    # rundll32.exe is a Windows utility that calls functions in DLL files
    # user32.dll contains the LockWorkStation function
    os.system("rundll32.exe user32.dll,LockWorkStation")
    return "🔒 Screen locked."

@register_command("shut down in 5 minutes", safe=False)
def shutdown_timer():
    """
    Schedule a system shutdown to occur in 5 minutes.
    
    This command uses the Windows shutdown utility to schedule a shutdown
    with a 5-minute delay. The delay provides time to save work and allows
    the user to cancel the shutdown if needed.
    
    Returns:
        str: Success message confirming the shutdown is scheduled
        
    Example:
        result = do("shut down in 5 minutes")
        # Result: "⏳ System will shut down in 5 minutes."
        
    Note:
        - Users can cancel with: shutdown /a
        - This command is marked as safe=False due to its significant impact
        - The 5-minute delay is a safety feature to prevent accidental shutdowns
    """
    # Use Windows shutdown command with parameters:
    # /s = shutdown (not restart)
    # /t 300 = timeout of 300 seconds (5 minutes)
    os.system("shutdown /s /t 300")
    return "⏳ System will shut down in 5 minutes."

@register_command("restart in 5 minutes", safe=False)
def restart_timer():
    """
    Schedule a system restart to occur in 5 minutes.
    
    This command schedules a system reboot with a 5-minute delay, allowing
    time to save work and providing the opportunity to cancel if needed.
    
    Returns:
        str: Success message confirming the restart is scheduled
        
    Example:
        result = do("restart in 5 minutes")
        # Result: "🔄 System will restart in 5 minutes."
        
    Note:
        - Users can cancel with: shutdown /a
        - This command is marked as safe=False due to its significant impact
        - The 5-minute delay helps prevent accidental restarts
    """
    # Use Windows shutdown command with parameters:
    # /r = restart (reboot)
    # /t 300 = timeout of 300 seconds (5 minutes)
    os.system("shutdown /r /t 300")
    return "🔄 System will restart in 5 minutes."

@register_command("hibernate", safe=False)
def hibernate():
    """
    Put the system into hibernation mode.
    
    Hibernation saves the current session to disk and powers off the computer.
    When powered back on, the system restores the exact state it was in,
    including open applications and documents.
    
    Returns:
        str: Success message (may not be seen if hibernation is immediate)
        
    Example:
        result = do("hibernate")
        # Result: "💤 System hibernated."
        # (System immediately enters hibernation)
        
    Note:
        - Hibernation must be enabled in system power settings
        - Some systems may not support hibernation
        - This command is marked as safe=False due to its system impact
        - The return message may not be visible as the system powers down
    """
    # Use Windows shutdown command with hibernate parameter:
    # /h = hibernate
    os.system("shutdown /h")
    return "💤 System hibernated."

# Utility functions for system power management

def _cancel_scheduled_shutdown():
    """
    Cancel any pending shutdown or restart.
    
    This utility function can be used to cancel shutdown/restart commands
    that were previously scheduled.
    
    Returns:
        str: Result of the cancellation attempt
    """
    try:
        result = os.system("shutdown /a")
        if result == 0:
            return "✅ Scheduled shutdown/restart cancelled"
        else:
            return "❌ No shutdown was scheduled or cancellation failed"
    except Exception as e:
        return f"❌ Error cancelling shutdown: {e}"

def _check_hibernation_support():
    """
    Check if hibernation is supported and enabled on this system.
    
    This is a placeholder function that could be implemented to verify
    hibernation capability before attempting to hibernate.
    
    Returns:
        bool: True if hibernation is supported, False otherwise
    """
    # This is a simplified check - a full implementation might check:
    # - Power settings via powercfg command
    # - Available disk space for hibernation file
    # - System capabilities
    return True  # Assume supported for now

