"""
CaelumSys - Human-friendly system automation toolkit

CaelumSys provides a simple, natural language interface for system automation.
Instead of remembering complex APIs, just use plain English commands.

Usage:
    from caelum_sys import do
    
    # Execute commands with natural language
    result = do("mute volume")
    result = do("create file at test.txt")
    result = do("take screenshot")
    
    print(result)  # Get human-readable feedback

Features:
    - 39+ built-in commands across multiple categories
    - Plugin-based architecture for easy extension
    - Automatic plugin discovery and loading
    - Natural language command processing
    - Cross-platform support (Windows focus)
    
Command Categories:
    - File Management (create, delete, copy, move files/folders)
    - Media Controls (volume, music playback)
    - System Information (CPU, memory, network info)
    - Screenshots (capture screen with various options)
    - Process Management (list, kill processes)
    - Windows Tools (task manager, file explorer, etc.)
    - Network Tools (ping, DNS, IP info)
"""

# Import the main execution function - this is what users will primarily use
from .core_actions import do

# Import utility function to discover available commands
from .registry import get_registered_command_phrases

# Auto-load all plugins when package is imported
# This ensures all commands are available immediately after import
from .plugins import load_plugins
load_plugins()

# Package metadata
__version__ = "0.1.5"
__author__ = "Joshua Wells"
__email__ = "your-email@example.com"  # Update with your actual email
__description__ = "Human-friendly system automation toolkit"

# Public API - these functions are available when users import the package
__all__ = [
    "do",                           # Main function to execute commands
    "get_registered_command_phrases" # Function to list all available commands
]
