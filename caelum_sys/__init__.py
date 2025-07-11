"""
CaelumSys - Human-friendly system automation toolkit

Usage:
    from caelum_sys import do
    
    # Execute commands
    result = do("mute volume")
    result = do("create file at test.txt")
    result = do("take screenshot")
"""

from .core_actions import do
from .registry import get_registered_command_phrases

# Auto-load all plugins when package is imported
from .plugins import load_plugins
load_plugins()

__version__ = "0.1.3"
__all__ = ["do", "get_registered_command_phrases"]
