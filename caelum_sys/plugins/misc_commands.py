"""
CaelumSys Miscellaneous Commands Plugin

This plugin provides various utility commands that don't fit into other specific 
categories. These include time and date information, system information queries,
and basic greeting functionality. All commands are informational and safe.

Commands provided:
- Time and System Information:
  * "get current time" - Display current timestamp with date and time
  * "get system info" - Show detailed system platform information
  * "get python version" - Display the Python interpreter version
  
- Interactive Commands:
  * "say hello" - Simple greeting response from the system

All commands in this plugin are marked as safe=True since they only
provide information and don't modify system state or perform destructive operations.

Dependencies:
- datetime: For current time operations
- platform: For system and Python version information

Usage Examples:
    >>> from caelum_sys.core_actions import do
    >>> do("get current time")
    "⏰ Current time: 2024-01-15 14:30:45"
    
    >>> do("get system info") 
    "🖥️ System Info:
    System: Windows
    Node: MyComputer
    ..."
"""

from caelum_sys.registry import register_command
import datetime
import platform

@register_command("get current time")
def get_time():
    """
    Get the current date and time in 24-hour format.
    
    Returns:
        str: Current timestamp formatted as "YYYY-MM-DD HH:MM:SS"
        
    Example:
        >>> get_time()
        "⏰ Current time: 2024-01-15 14:30:45"
    """
    now = datetime.datetime.now()
    return f"⏰ Current time: {now.strftime('%Y-%m-%d %H:%M:%S')}"

@register_command("get system info")
def get_system_info():
    """
    Get detailed system platform information.
    
    This function retrieves comprehensive information about the current
    system including operating system, hostname, version details, 
    architecture, and processor information.
    
    Returns:
        str: Multi-line string containing detailed system information
        
    Example:
        >>> get_system_info()
        "🖥️ System Info:
        System: Windows
        Node: MyComputer
        Release: 10
        Version: 10.0.19041
        Machine: AMD64
        Processor: Intel64 Family..."
    """
    info = platform.uname()
    return f"🖥️ System Info:\n" \
           f"System: {info.system}\n" \
           f"Node: {info.node}\n" \
           f"Release: {info.release}\n" \
           f"Version: {info.version}\n" \
           f"Machine: {info.machine}\n" \
           f"Processor: {info.processor}"

@register_command("say hello")
def say_hello():
    """
    Simple greeting function that responds with a friendly message.
    
    This is a basic interactive command that can be used to test
    system responsiveness or as a simple demonstration of the
    command system functionality.
    
    Returns:
        str: Friendly greeting message with emoji
        
    Example:
        >>> say_hello()
        "👋 Hello from Caelum-Sys!"
    """
    return "👋 Hello from Caelum-Sys!"

@register_command("get python version")
def get_python_version():
    """
    Get the version of the Python interpreter currently running.
    
    This is useful for debugging and ensuring compatibility when
    running scripts or checking system requirements.
    
    Returns:
        str: Python version string in major.minor.patch format
        
    Example:
        >>> get_python_version()
        "🐍 Python Version: 3.11.7"
    """
    return f"🐍 Python Version: {platform.python_version()}"
