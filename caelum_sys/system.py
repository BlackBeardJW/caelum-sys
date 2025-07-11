"""
CaelumSys Legacy System Operations Module

This module provides low-level system operation functions for the legacy command
system. It contains cross-platform implementations for basic system tasks like
application launching, process management, and system shutdown.

⚠️ LEGACY MODULE NOTICE:
This module is part of the legacy command system that predates the current
plugin-based architecture. Modern CaelumSys uses specialized plugins in the
plugins/ directory for system operations with better error handling and
feature coverage.

Supported Operations:
- Application launching with cross-platform compatibility
- Process listing and management using psutil
- System shutdown with platform-specific commands
- Process termination by name matching

Platform Support:
- Windows: Uses 'start' command and Windows shutdown utilities
- macOS (Darwin): Uses 'open' command and sudo shutdown
- Linux/Unix: Uses direct executable launching and shutdown commands

Dependencies:
- platform: For operating system detection
- subprocess: For launching external applications and commands
- psutil: For process management and system monitoring
- os: For system command execution

Note:
Modern CaelumSys plugins provide more robust implementations with better
error handling, safety features, and extended functionality.
"""

import platform
import subprocess
import psutil
import os

def open_application(app_name):
    """
    Launch an application by name using platform-specific methods.
    
    This function attempts to open an application using the appropriate
    system command for the current operating system. It provides cross-platform
    compatibility for basic application launching.
    
    Args:
        app_name (str): Name or path of the application to launch
                       Can be executable name, full path, or app identifier
    
    Returns:
        str: Success message if launch initiated, error message if failed
    
    Platform-Specific Behavior:
        
        Windows:
        - Uses: start "" [app_name]
        - Supports: executable names, file paths, URLs
        - Examples: "notepad", "calc", "chrome.exe"
        
        macOS (Darwin):
        - Uses: open -a [app_name]
        - Supports: application names, bundle identifiers
        - Examples: "TextEdit", "Safari", "com.apple.Calculator"
        
        Linux/Unix:
        - Uses: [app_name] (direct execution)
        - Supports: executable names in PATH, full paths
        - Examples: "gedit", "firefox", "/usr/bin/calculator"
    
    Examples:
        >>> open_application("notepad")  # Windows
        "Opening notepad..."
        
        >>> open_application("TextEdit")  # macOS
        "Opening TextEdit..."
        
        >>> open_application("gedit")  # Linux
        "Opening gedit..."
        
        >>> open_application("nonexistent-app")
        "Failed to open nonexistent-app: [FileNotFoundError details]"
    
    Error Handling:
        - Catches all exceptions during application launch
        - Returns descriptive error message with exception details
        - Does not validate application existence before launch attempt
    
    Note:
        This is a legacy implementation. Modern plugins provide more
        sophisticated application management with validation and error handling.
    """
    try:
        if platform.system() == "Windows":
            # Windows: Use 'start' command with empty title parameter
            subprocess.Popen(["start", "", app_name], shell=True)
        elif platform.system() == "Darwin":
            # macOS: Use 'open -a' to launch applications
            subprocess.Popen(["open", "-a", app_name])
        else:
            # Linux/Unix: Direct executable launch
            subprocess.Popen([app_name])
        return f"Opening {app_name}..."
    except Exception as e:
        return f"Failed to open {app_name}: {e}"

def list_processes():
    """
    List all running processes with their PIDs and names.
    
    This function retrieves information about all currently running processes
    on the system using psutil. It returns a formatted string containing
    process IDs and names for system monitoring purposes.
    
    Returns:
        str: Multi-line string with process information
             Format: "PID: process_name" (one per line)
    
    Examples:
        >>> list_processes()
        "1234: chrome.exe
        5678: notepad.exe
        9012: python.exe
        3456: explorer.exe
        ..."
    
    Process Information:
        - PID: Process identifier (unique integer)
        - Name: Process executable name (e.g., "chrome.exe", "python")
        - Only accessible processes are included (may miss some system processes)
    
    Performance Notes:
        - Can be slow on systems with many running processes
        - Process list is a snapshot at the time of execution
        - Some processes may not be visible due to security restrictions
    
    Error Handling:
        - Individual process access errors are silently ignored
        - Inaccessible processes are skipped from the output
        - psutil handles platform-specific process enumeration
    
    Note:
        Modern process management plugins provide more detailed information
        including CPU usage, memory usage, and advanced filtering options.
    """
    # Get list of all running processes with PID and name information
    processes = [(p.pid, p.name()) for p in psutil.process_iter()]
    
    # Format as "PID: name" strings and join with newlines
    return "\n".join([f"{pid}: {name}" for pid, name in processes])

def kill_process(name):
    """
    Terminate all processes whose names contain the specified string.
    
    ⚠️ DESTRUCTIVE OPERATION WARNING:
    This function forcibly terminates processes and may cause data loss
    if processes have unsaved work. Use with extreme caution.
    
    This function searches for all running processes that contain the given
    name substring (case-insensitive) and attempts to terminate them using
    the kill() method.
    
    Args:
        name (str): Process name or substring to search for
                   Matching is case-insensitive and uses substring containment
    
    Returns:
        str: Success message with process count or failure message
    
    Examples:
        >>> kill_process("notepad")
        "Killed process(es) named 'notepad'"
        
        >>> kill_process("chrome")
        "Killed process(es) named 'chrome'"
        
        >>> kill_process("nonexistent")
        "No process found named 'nonexistent'"
    
    Matching Behavior:
        - Case-insensitive substring matching
        - Multiple processes can be killed if they match
        - Partial name matching (e.g., "note" matches "notepad.exe")
    
    Process Termination:
        - Uses psutil.Process.kill() for immediate termination
        - SIGKILL equivalent (forceful termination)
        - No graceful shutdown or save prompts
        - May require elevated privileges for some processes
    
    Error Handling:
        - Individual process termination errors are silently ignored
        - Continues attempting to kill other matching processes
        - Reports success if any processes were terminated
    
    Security Considerations:
        - Can terminate critical system processes
        - May require administrative privileges
        - Some processes may be protected from termination
        
    Note:
        Modern process management plugins provide safer termination options
        with confirmation prompts and process validation.
    """
    found = False
    
    # Iterate through all running processes
    for proc in psutil.process_iter():
        # Check if the target name is contained in the process name (case-insensitive)
        if name.lower() in proc.name().lower():
            try:
                proc.kill()  # Forcefully terminate the process
                found = True
            except (psutil.NoSuchProcess, psutil.AccessDenied):
                # Ignore processes that can't be killed or no longer exist
                continue
    
    # Return appropriate success or failure message
    return f"Killed process(es) named '{name}'" if found else f"No process found named '{name}'"

def shutdown_system():
    """
    Initiate system shutdown using platform-specific commands.
    
    ⚠️ CRITICAL SYSTEM OPERATION WARNING:
    This function will shut down the computer and may cause data loss if
    applications have unsaved work. This is a destructive operation that
    should be used with extreme caution.
    
    This function uses operating system-specific shutdown commands to initiate
    an immediate system shutdown. The implementation varies by platform but
    all result in system power-off.
    
    Returns:
        str: Success message if shutdown initiated, error message if failed
             Note: Success message may not be visible as system shuts down
    
    Platform-Specific Commands:
        
        Windows:
        - Command: shutdown /s /t 1
        - Effect: Shutdown in 1 second
        - Behavior: Immediate shutdown with minimal delay
        
        macOS (Darwin):
        - Command: sudo shutdown -h now  
        - Effect: Immediate halt and power off
        - Note: May require sudo password (will fail if not available)
        
        Linux/Unix:
        - Command: shutdown now
        - Effect: Immediate system shutdown
        - Note: May require sudo privileges depending on system configuration
    
    Examples:
        >>> shutdown_system()
        "System is shutting down..."
        # System begins shutdown process immediately
        
        >>> shutdown_system()  # On error
        "Shutdown failed: [PermissionError details]"
    
    Timing and Behavior:
        - Windows: 1-second delay before shutdown
        - macOS/Linux: Immediate shutdown attempt
        - All unsaved work will be lost
        - Running applications may be forcefully closed
        
    Error Conditions:
        - Insufficient privileges (most common)
        - System policy restrictions
        - Hardware or driver issues
        - Network authentication requirements (domain systems)
    
    Safety Considerations:
        - No confirmation prompt or safety delay
        - Cannot be easily cancelled once initiated
        - May cause data corruption if file operations are in progress
        - Other users may lose their work
        
    Note:
        Modern system utilities provide safer shutdown options with
        configurable delays, user notifications, and cancellation capabilities.
    """
    try:
        if platform.system() == "Windows":
            # Windows: Shutdown with 1-second timeout
            os.system("shutdown /s /t 1")
        elif platform.system() == "Darwin":
            # macOS: Immediate halt (requires sudo)
            os.system("sudo shutdown -h now")
        else:
            # Linux/Unix: Immediate shutdown
            os.system("shutdown now")
        return "System is shutting down..."
    except Exception as e:
        return f"Shutdown failed: {e}"
