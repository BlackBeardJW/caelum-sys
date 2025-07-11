"""
CaelumSys Process Management Tools Plugin

This plugin provides system process management and monitoring capabilities.
It includes functions for listing processes, monitoring resource usage,
and terminating processes. Some commands are marked as unsafe due to their
potential impact on system stability.

Commands provided:
- Process Information:
  * "list running processes" - List all currently running processes
  * "get cpu usage" - Show current CPU utilization percentage
  * "get memory usage" - Display memory usage statistics
  
- Process Control (UNSAFE):
  * "kill process by name {name}" - Terminate processes matching name

Safety Notes:
- Process listing and monitoring commands are safe (safe=True)
- Process termination is marked as unsafe (safe=False) as it can:
  * Cause data loss if process has unsaved work
  * Destabilize system if critical processes are killed
  * Terminate multiple processes if name matches broadly

Dependencies:
- psutil: Cross-platform library for system and process monitoring

Usage Examples:
    >>> from caelum_sys.core_actions import do
    >>> do("get cpu usage")
    "💻 CPU usage: 15.2%"
    
    >>> do("get memory usage") 
    "🧠 Memory usage: 67% used (8192MB / 12288MB)"
    
    >>> do("kill process by name notepad")  # UNSAFE OPERATION
    "☠️ Killed: notepad.exe"

WARNINGS:
- Use process termination commands with extreme caution
- Always verify process names before killing
- Some processes may require elevated privileges to terminate
"""

from caelum_sys.registry import register_command
import psutil

@register_command("list running processes")
def list_processes():
    """
    List all currently running processes on the system.
    
    This function retrieves the names of all active processes using psutil.
    The list can be quite long on typical systems with many background processes.
    
    Returns:
        str: Formatted list of all running process names
        
    Example:
        >>> list_processes()
        "🧠 Running Processes:
        System
        Registry
        smss.exe
        csrss.exe
        winlogon.exe
        ..."
        
    Note:
        - Process list is a snapshot at the time of execution
        - Some processes may not be visible due to security restrictions
        - Process names may include system processes and user applications
    """
    processes = [proc.info["name"] for proc in psutil.process_iter(attrs=["name"])]
    return f"🧠 Running Processes:\n" + "\n".join(processes)

@register_command("kill process by name {name}", safe=False)
def kill_process_by_name(name: str):
    """
    Terminate all processes whose names contain the specified string.
    
    ⚠️ WARNING: This is a DESTRUCTIVE operation marked as unsafe!
    
    This function searches for all running processes that have the given
    name substring in their process name and attempts to terminate them.
    Use with extreme caution as it can:
    - Cause data loss if processes have unsaved work
    - Destabilize the system if critical processes are killed
    - Kill multiple processes if the name matches broadly
    
    Args:
        name (str): Process name or substring to search for (case-insensitive)
        
    Returns:
        str: List of killed processes or message if none found
        
    Example:
        >>> kill_process_by_name("notepad")
        "☠️ Killed: notepad.exe"
        
        >>> kill_process_by_name("nonexistent")
        "⚠️ No process found with name matching 'nonexistent'"
        
    Security Notes:
        - May require administrative privileges for some processes
        - System-critical processes may be protected from termination
        - Some processes may restart automatically after being killed
        
    IMPORTANT: Always verify the process name before executing this command!
    """
    killed = []
    for proc in psutil.process_iter(attrs=["name"]):
        if proc.info["name"] and name.lower() in proc.info["name"].lower():
            try:
                proc.kill()
                killed.append(proc.info["name"])
            except psutil.NoSuchProcess:
                continue
    if killed:
        return f"☠️ Killed: {', '.join(killed)}"
    return f"⚠️ No process found with name matching '{name}'"

@register_command("get cpu usage")
def get_cpu_usage():
    """
    Get the current CPU utilization percentage.
    
    This function measures CPU usage over a 1-second interval to provide
    an accurate reading of current system load. The measurement includes
    all CPU cores averaged together.
    
    Returns:
        str: CPU usage percentage with appropriate emoji
        
    Example:
        >>> get_cpu_usage()
        "💻 CPU usage: 15.2%"
        
    Note:
        - Measurement takes 1 second to complete (uses interval=1)
        - Shows average across all CPU cores
        - High values (>80%) may indicate system stress
        - Low values (<10%) indicate light system load
    """
    cpu = psutil.cpu_percent(interval=1)
    return f"💻 CPU usage: {cpu}%"

@register_command("get memory usage")
def get_memory_usage():
    """
    Get current system memory (RAM) usage statistics.
    
    This function provides detailed memory usage information including
    percentage used and absolute values in megabytes for both used
    and total system memory.
    
    Returns:
        str: Memory usage percentage and absolute values in MB
        
    Example:
        >>> get_memory_usage()
        "🧠 Memory usage: 67% used (8192MB / 12288MB)"
        
    Note:
        - Shows virtual memory (RAM) usage, not disk space
        - Values are rounded to nearest MB for readability
        - High usage (>90%) may cause system slowdown
        - Includes memory used by all processes and system
    """
    mem = psutil.virtual_memory()
    return f"🧠 Memory usage: {mem.percent}% used ({mem.used // (1024 ** 2)}MB / {mem.total // (1024 ** 2)}MB)"
