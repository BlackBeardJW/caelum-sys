"""
CaelumSys Command Line Interface (CLI) Module

This module provides the main entry point for the CaelumSys package when used
as a command-line tool. It handles command-line argument parsing and delegates
execution to the core action system.

The CLI allows users to execute CaelumSys commands directly from the terminal
without needing to write Python scripts. It serves as a bridge between the
command line and the internal command processing system.

Usage:
    Command line: caelum-sys "your command here"
    Python: from caelum_sys.cli import main; main()

Examples:
    $ caelum-sys "take screenshot"
    $ caelum-sys "get system info"
    $ caelum-sys "play music"

Entry Point:
    This module is configured as the entry point in setup.py/pyproject.toml,
    allowing the 'caelum-sys' command to be available system-wide after
    package installation.

Dependencies:
    - sys: For command-line argument processing
    - core_actions: For command execution via the do() function
"""

import sys
from .core_actions import do

def main():
    """
    Main entry point for the CaelumSys command-line interface.
    
    This function processes command-line arguments and executes the specified
    command using the CaelumSys command processing system. It expects at least
    one argument containing the command to execute.
    
    Command-line Arguments:
        sys.argv[1:]: The command string and its parameters
                     Multiple arguments are joined with spaces
    
    Usage:
        caelum-sys "command to execute"
        caelum-sys "command with parameters like {param}"
    
    Examples:
        $ caelum-sys "take screenshot"
        $ caelum-sys "ping google.com"
        $ caelum-sys "create file example.txt"
    
    Error Handling:
        - Displays usage message if no command is provided
        - Command execution errors are handled by the core_actions.do() function
    
    Returns:
        None: Output is printed directly to stdout by the do() function
        
    Note:
        This function is designed to be called from the command line via
        the entry point configuration, not typically from Python code.
    """
    # Check if at least one argument (the command) was provided
    if len(sys.argv) < 2:
        print("Usage: caelum-sys \"<command>\"")
        return
    
    # Join all command-line arguments into a single command string
    # This allows commands with spaces and parameters to work correctly
    command = " ".join(sys.argv[1:])
    
    # Execute the command using the core CaelumSys processing system
    do(command)
