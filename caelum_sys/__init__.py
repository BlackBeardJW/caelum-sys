"""CaelumSys - Human-friendly system automation toolkit"""

from .core_actions import do
from .registry import get_registered_command_phrases
from .auto_import_plugins import load_all_plugins

# Auto-load all plugins when package is imported
load_all_plugins()

__version__ = "0.3.0"
__author__ = "Joshua Wells" 
__description__ = "System automation toolkit with 117+ commands across 16 plugins"

__all__ = ["do", "get_registered_command_phrases"]
