from caelum_sys.registry import register_command
import socket
import subprocess

@register_command("get my ip address")
def get_ip_address():
    """Returns the local IP address of the machine."""
    ip = socket.gethostbyname(socket.gethostname())
    return f"🌐 Local IP address: {ip}"

@register_command("ping {host}")
def ping_host(host: str):
    """Pings a given host and returns the result."""
    try:
        output = subprocess.check_output(["ping", "-n", "4", host], text=True)
        return f"📡 Ping results for {host}:\n{output}"
    except subprocess.CalledProcessError:
        return f"❌ Failed to ping {host}."

@register_command("get hostname")
def get_hostname():
    """Returns the system hostname."""
    hostname = socket.gethostname()
    return f"🖥️ Hostname: {hostname}"

@register_command("resolve dns for {domain}")
def resolve_dns(domain: str):
    """Resolves the IP address of a given domain."""
    try:
        ip = socket.gethostbyname(domain)
        return f"🔍 {domain} resolved to {ip}"
    except socket.gaierror:
        return f"❌ Failed to resolve {domain}"
