"""
CaelumSys Legacy Command Parser Module

This module provides natural language command parsing functionality for the
legacy command system. It uses regular expressions to extract intents and
arguments from user input strings.

⚠️ LEGACY MODULE NOTICE:
This module is part of the legacy command system that predates the current
plugin-based architecture. Modern CaelumSys uses the advanced natural language
processing in core_actions.py with fuzzy matching and parameter extraction.

Parsing Strategy:
- Uses regex patterns to match command structures
- Converts natural language to intent + argument pairs
- Case-insensitive matching for user convenience
- Supports basic parameter extraction

Supported Command Patterns:
- "open [application]" -> ("open_app", application_name)
- "list processes" -> ("list_processes", None)
- "kill [process]" -> ("kill_process", process_name)  
- "shutdown" -> ("shutdown", None)
- Unrecognized commands -> ("unknown", original_command)

Dependencies:
- re: For regular expression pattern matching

Note:
The modern CaelumSys architecture uses more sophisticated parsing in
core_actions.py that supports fuzzy matching, parameter extraction,
and plugin-based command registration.
"""

import re

def parse_command(command: str):
    """
    Parse a natural language command into intent and argument components.
    
    This function analyzes user input to determine the intended action and
    extract relevant parameters. It uses regular expressions to match
    predefined command patterns and convert them into structured data.
    
    Args:
        command (str): The natural language command string to parse
                      Commands are converted to lowercase for consistency
    
    Returns:
        tuple: (intent, argument) where:
               intent (str): The identified command action/intent
               argument (str|None): Extracted parameter or None if not needed
    
    Supported Command Patterns:
        
        Application Control:
        - "open [app]" -> ("open_app", app_name)
          Examples: "open notepad", "open chrome"
        
        Process Management:
        - "list processes" -> ("list_processes", None)
        - "kill [process]" -> ("kill_process", process_name)
          Examples: "kill notepad", "kill chrome"
        
        System Control:
        - "shutdown" -> ("shutdown", None)
        
        Fallback:
        - Unrecognized -> ("unknown", original_command)
    
    Examples:
        >>> parse_command("open notepad")
        ("open_app", "notepad")
        
        >>> parse_command("LIST PROCESSES")  # Case insensitive
        ("list_processes", None)
        
        >>> parse_command("kill chrome")
        ("kill_process", "chrome")
        
        >>> parse_command("shutdown system")
        ("shutdown", None)
        
        >>> parse_command("invalid command")
        ("unknown", "invalid command")
    
    Implementation Details:
        - Commands are converted to lowercase for consistent matching
        - Uses re.match() for start-of-string pattern matching
        - Uses re.findall() to extract parameter values
        - String containment check for simple keyword commands
        
    Limitations:
        - Fixed set of supported command patterns
        - No fuzzy matching or typo tolerance
        - Simple parameter extraction (single argument only)
        - No support for complex parameter structures
        
    Note:
        This parser is part of the legacy system. The modern CaelumSys
        uses advanced parsing with fuzzy matching and parameter extraction
        in the core_actions.py module.
    """
    # Convert to lowercase for case-insensitive matching
    command = command.lower()
    
    # Pattern: "open [application_name]"
    if re.match(r"open (.+)", command):
        app = re.findall(r"open (.+)", command)[0]
        return ("open_app", app)
    
    # Pattern: "list processes" (exact keyword match)
    elif "list processes" in command:
        return ("list_processes", None)
    
    # Pattern: "kill [process_name]"
    elif re.match(r"kill (.+)", command):
        proc = re.findall(r"kill (.+)", command)[0]
        return ("kill_process", proc)
    
    # Pattern: "shutdown" (keyword containment)
    elif "shutdown" in command:
        return ("shutdown", None)
    
    # Fallback for unrecognized commands
    return ("unknown", command)
