"""
CaelumSys Legacy Command Executor Module

This module provides a legacy command execution system that predates the current
plugin-based architecture. It contains hardcoded command patterns and execution
logic for basic system operations.

⚠️ LEGACY MODULE NOTICE:
This module appears to be from an earlier version of CaelumSys and may not be
actively used by the current plugin-based system. The modern architecture uses
the registry system with @register_command decorators instead of this hardcoded
approach.

Supported Legacy Commands:
- "open [app]" - Open applications by name
- "list processes" - List running system processes  
- "kill [process]" - Terminate processes by name
- "shutdown" - Shut down the system

Architecture:
- Uses intent-based parsing from parser.py
- Delegates system operations to system.py
- Simple string matching for command recognition

Dependencies:
- system: For actual system operation execution
- parser: For command parsing and intent extraction

Note:
Modern CaelumSys commands should use the plugin system in the plugins/
directory with @register_command decorators for better maintainability
and extensibility.
"""

from . import system
from .parser import parse_command

def execute(intent, arg):
    """
    Execute a command based on parsed intent and arguments.
    
    This function takes a parsed command intent and its associated argument,
    then routes the execution to the appropriate system function. It serves
    as a dispatcher between the command parser and system operations.
    
    Args:
        intent (str): The parsed command intent/action to perform
                     Valid intents: "open_app", "list_processes", 
                     "kill_process", "shutdown"
        arg (str|None): The argument associated with the intent
                       None for commands that don't require arguments
    
    Returns:
        str: Result message from the executed system operation
             or error message for unknown commands
    
    Supported Intent Mappings:
        - "open_app" + app_name -> system.open_application(app_name)
        - "list_processes" + None -> system.list_processes()
        - "kill_process" + process_name -> system.kill_process(process_name)
        - "shutdown" + None -> system.shutdown_system()
    
    Examples:
        >>> execute("open_app", "notepad")
        "Opening notepad..."
        
        >>> execute("list_processes", None)
        "1234: chrome.exe\n5678: notepad.exe\n..."
        
        >>> execute("kill_process", "notepad")
        "Killed process(es) named 'notepad'"
        
        >>> execute("unknown_intent", "some_arg")
        "Unknown command: some_arg"
    
    Error Handling:
        - Unknown intents return an error message
        - System operation errors are handled by the respective system functions
        
    Note:
        This is part of the legacy command system. Modern CaelumSys uses
        the plugin architecture for command registration and execution.
    """
    if intent == "open_app":
        return system.open_application(arg)
    elif intent == "list_processes":
        return system.list_processes()
    elif intent == "kill_process":
        return system.kill_process(arg)
    elif intent == "shutdown":
        return system.shutdown_system()
    else:
        return f"Unknown command: {arg}"
