"""
CaelumSys Network Tools Plugin

This plugin provides network-related utility commands for basic connectivity testing,
DNS resolution, and local network information. These tools are useful for network
troubleshooting and system administration tasks.

Commands provided:
- Network Information:
  * "get my ip address" - Get the local IP address of this machine
  * "get hostname" - Get the system hostname/computer name
  
- Network Testing:
  * "ping {host}" - Test connectivity to a host (4 packets on Windows)
  * "resolve dns for {domain}" - Resolve domain name to IP address

Safety Notes:
- All commands are marked as safe=True
- ping command uses Windows-specific flags (-n 4) 
- Network commands may timeout or fail due to connectivity issues
- DNS resolution depends on current DNS server configuration

Dependencies:
- socket: For network operations and hostname resolution
- subprocess: For executing system ping commands

Usage Examples:
    >>> from caelum_sys.core_actions import do
    >>> do("get my ip address")
    "🌐 Local IP address: 192.168.1.100"
    
    >>> do("ping google.com")
    "📡 Ping results for google.com:
    Pinging google.com [142.250....]"
    
    >>> do("resolve dns for github.com")
    "🔍 github.com resolved to 140.82.113.4"
"""

from caelum_sys.registry import register_command
import socket
import subprocess

@register_command("get my ip address")
def get_ip_address():
    """
    Get the local IP address of this machine.
    
    This function attempts to determine the local IP address by resolving
    the hostname. Note that this may return 127.0.0.1 (localhost) on some
    systems or in certain network configurations.
    
    Returns:
        str: Local IP address with network emoji
        
    Example:
        >>> get_ip_address()
        "🌐 Local IP address: 192.168.1.100"
        
    Note:
        On some systems this may return the loopback address (127.0.0.1)
        instead of the actual network interface IP.
    """
    ip = socket.gethostbyname(socket.gethostname())
    return f"🌐 Local IP address: {ip}"

@register_command("ping {host}")
def ping_host(host: str):
    """
    Ping a specified host to test network connectivity.
    
    This function sends 4 ICMP echo requests to the specified host
    using the Windows ping command. It's useful for testing network
    connectivity and measuring round-trip times.
    
    Args:
        host (str): The hostname or IP address to ping
        
    Returns:
        str: Ping results including statistics, or error message
        
    Example:
        >>> ping_host("google.com")
        "📡 Ping results for google.com:
        Pinging google.com [142.250.191.14] with 32 bytes of data:
        Reply from 142.250.191.14: bytes=32 time=23ms TTL=116
        ..."
        
        >>> ping_host("nonexistent.invalid")
        "❌ Failed to ping nonexistent.invalid."
        
    Note:
        - Uses Windows-specific ping flags (-n 4 for 4 packets)
        - May require administrative privileges on some systems
        - Will timeout for unreachable hosts
    """
    try:
        output = subprocess.check_output(["ping", "-n", "4", host], text=True)
        return f"📡 Ping results for {host}:\n{output}"
    except subprocess.CalledProcessError:
        return f"❌ Failed to ping {host}."

@register_command("get hostname")
def get_hostname():
    """
    Get the system hostname (computer name).
    
    Returns the network name/hostname of the current machine as
    configured in the system settings.
    
    Returns:
        str: System hostname with computer emoji
        
    Example:
        >>> get_hostname()
        "🖥️ Hostname: MyComputer"
        
    Note:
        This returns the local hostname, not the fully qualified domain name.
    """
    hostname = socket.gethostname()
    return f"🖥️ Hostname: {hostname}"

@register_command("resolve dns for {domain}")
def resolve_dns(domain: str):
    """
    Resolve a domain name to its IP address using DNS lookup.
    
    This function performs a DNS A record lookup to convert a domain
    name into its corresponding IPv4 address. Useful for verifying
    DNS resolution and troubleshooting connectivity issues.
    
    Args:
        domain (str): The domain name to resolve (e.g., "google.com")
        
    Returns:
        str: Domain name and its resolved IP address, or error message
        
    Example:
        >>> resolve_dns("github.com")
        "🔍 github.com resolved to 140.82.113.4"
        
        >>> resolve_dns("invalid.domain.xyz")
        "❌ Failed to resolve invalid.domain.xyz"
        
    Note:
        - Uses the system's configured DNS servers
        - May return different IPs for load-balanced services
        - Requires internet connectivity for external domains
    """
    try:
        ip = socket.gethostbyname(domain)
        return f"🔍 {domain} resolved to {ip}"
    except socket.gaierror:
        return f"❌ Failed to resolve {domain}"
