"""
CaelumSys Windows-Specific Tools Plugin

This plugin provides Windows-specific system utilities and administrative tools.
All commands are protected by the @safe_windows decorator, which ensures they
only execute on Windows systems and return an appropriate error message on
other platforms.

Commands provided:
- System Administration:
  * "open task manager" - Launch Windows Task Manager
  * "open device manager" - Open Device Manager console
  * "open control panel" - Launch Windows Control Panel
  
- File System Access:
  * "open file explorer" - Open Windows File Explorer
  
- Security:
  * "lock workstation" - Lock the current user session

Platform Compatibility:
- All commands check platform.system() == "Windows"
- Non-Windows systems receive informative error messages
- Commands use Windows-specific executables and system calls

Safety Features:
- All commands are marked as safe=True (launch system tools)
- Lock workstation provides immediate security without data loss
- No destructive operations or system modifications

Dependencies:
- platform: For OS detection
- subprocess: For launching Windows system utilities

Usage Examples:
    >>> from caelum_sys.core_actions import do
    >>> do("open task manager")  # On Windows
    "🧰 Task Manager opened."
    
    >>> do("open task manager")  # On Linux/Mac
    "❌ This command is only available on Windows."

All launched applications run independently and don't block the command system.
"""

from caelum_sys.registry import register_command
import platform
import subprocess

# Platform detection constant for all Windows-specific operations
IS_WINDOWS = platform.system() == "Windows"

def safe_windows(func):
    """
    Decorator to ensure commands only execute on Windows systems.
    
    This decorator wraps Windows-specific functions to check the current
    platform before execution. If not running on Windows, it returns
    an informative error message instead of attempting to run Windows-only
    commands that would fail.
    
    Args:
        func: The function to wrap with Windows platform checking
        
    Returns:
        function: Wrapped function with platform safety check
        
    Example:
        @safe_windows
        def windows_only_function():
            return "This only works on Windows"
    """
    def wrapper(*args, **kwargs):
        if not IS_WINDOWS:
            return "❌ This command is only available on Windows."
        return func(*args, **kwargs)
    return wrapper

@register_command("open task manager")
@safe_windows
def open_task_manager():
    """
    Launch the Windows Task Manager application.
    
    Opens the built-in Windows Task Manager (taskmgr.exe) which provides
    system monitoring, process management, and performance information.
    The application launches in a separate process and runs independently.
    
    Returns:
        str: Confirmation message that Task Manager was opened
        
    Example:
        >>> open_task_manager()
        "🧰 Task Manager opened."
        
    Use Cases:
        - Monitor system performance and resource usage
        - View and manage running processes and services
        - Check startup programs and system impact
        - End unresponsive applications
        
    Note:
        - Launches in non-blocking mode (separate process)
        - May require User Account Control (UAC) permission on some systems
        - Administrative features require elevated privileges
    """
    subprocess.Popen("taskmgr")
    return "🧰 Task Manager opened."

@register_command("open file explorer")
@safe_windows
def open_file_explorer():
    """
    Launch the Windows File Explorer application.
    
    Opens the Windows File Explorer (explorer.exe) for browsing files
    and folders. The explorer window opens to the default location
    (typically "This PC" or user's home directory).
    
    Returns:
        str: Confirmation message that File Explorer was opened
        
    Example:
        >>> open_file_explorer()
        "📁 File Explorer opened."
        
    Use Cases:
        - Browse and navigate the file system
        - Copy, move, and organize files and folders
        - Access network locations and drives
        - Manage file properties and permissions
        
    Note:
        - Opens a new explorer window
        - Launches in non-blocking mode
        - Multiple explorer windows can be opened simultaneously
    """
    subprocess.Popen("explorer")
    return "📁 File Explorer opened."

@register_command("lock workstation")
@safe_windows
def lock_workstation():
    """
    Lock the current Windows user session.
    
    Immediately locks the workstation by calling the Windows API function
    LockWorkStation through rundll32.exe. This secures the computer by
    requiring password authentication to regain access while preserving
    all running applications and their state.
    
    Returns:
        str: Confirmation message that workstation was locked
        
    Example:
        >>> lock_workstation()
        "🔒 Workstation locked."
        
    Security Features:
        - Immediate session lock without delay
        - Preserves all application state and data
        - Requires user password to unlock
        - Activates screen saver or lock screen
        
    Use Cases:
        - Quick security when stepping away from computer
        - Compliance with security policies
        - Privacy protection in shared environments
        - Remote locking via automation scripts
        
    Note:
        - Command executes immediately
        - No confirmation dialog or delay
        - Equivalent to Windows+L keyboard shortcut
    """
    subprocess.Popen("rundll32.exe user32.dll,LockWorkStation")
    return "🔒 Workstation locked."

@register_command("open control panel")
@safe_windows
def open_control_panel():
    """
    Launch the Windows Control Panel application.
    
    Opens the classic Windows Control Panel (control.exe) which provides
    access to system configuration, hardware settings, user accounts,
    and various administrative tools.
    
    Returns:
        str: Confirmation message that Control Panel was opened
        
    Example:
        >>> open_control_panel()
        "⚙️ Control Panel opened."
        
    Available Categories:
        - System and Security (Windows Defender, System info)
        - Network and Internet (Network settings, Internet options)
        - Hardware and Sound (Devices, Audio settings)
        - Programs (Uninstall programs, Default programs)
        - User Accounts (User settings, Credential Manager)
        - Appearance and Personalization (Themes, Display)
        - Clock and Region (Date/time, Regional settings)
        - Ease of Access (Accessibility options)
        
    Note:
        - Some settings may require administrator privileges
        - Modern Windows versions also have Settings app
        - Control Panel provides access to legacy configuration options
    """
    subprocess.Popen("control")
    return "⚙️ Control Panel opened."

@register_command("open device manager")
@safe_windows
def open_device_manager():
    """
    Launch the Windows Device Manager console.
    
    Opens Device Manager (devmgmt.msc) which provides detailed information
    about all hardware devices installed on the system. Allows viewing
    device properties, updating drivers, and troubleshooting hardware issues.
    
    Returns:
        str: Confirmation message that Device Manager was opened
        
    Example:
        >>> open_device_manager()
        "🖥️ Device Manager opened."
        
    Device Categories:
        - Audio inputs and outputs
        - Disk drives and storage devices
        - Display adapters (graphics cards)
        - Network adapters (Ethernet, Wi-Fi)
        - Processors (CPU information)
        - Universal Serial Bus controllers
        - Human Interface Devices (keyboard, mouse)
        
    Administrative Functions:
        - Update device drivers
        - Enable/disable devices
        - View device properties and resources
        - Troubleshoot device problems
        - Scan for hardware changes
        
    Note:
        - Administrative privileges may be required for device modifications
        - Useful for diagnosing hardware conflicts and driver issues
        - Shows device status and any error conditions
    """
    subprocess.Popen(["devmgmt.msc"])
    return "🖥️ Device Manager opened."
