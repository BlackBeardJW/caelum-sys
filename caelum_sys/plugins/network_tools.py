"""
Network tools plugin for basic connectivity and DNS operations.
"""

import socket
import subprocess

from caelum_sys.registry import register_command


@register_command("get my ip address")
def get_ip_address():
    """Get the local IP address."""
    ip = socket.gethostbyname(socket.gethostname())
    return f"🌐 Local IP address: {ip}"


@register_command("ping {host}")
def ping_host(host: str):
    """Ping a host to test connectivity (4 packets)."""
    try:
        output = subprocess.check_output(["ping", "-n", "4", host], text=True)
        return f"📡 Ping results for {host}:\n{output}"
    except subprocess.CalledProcessError:
        return f"❌ Failed to ping {host}."


@register_command("get hostname")
def get_hostname():
    """Get the system hostname."""
    hostname = socket.gethostname()
    return f"🖥️ Hostname: {hostname}"


@register_command("resolve dns for {domain}")
def resolve_dns(domain: str):
    """Resolve a domain name to its IP address."""
    try:
        ip = socket.gethostbyname(domain)
        return f"🔍 {domain} resolved to {ip}"
    except socket.gaierror:
        return f"❌ Failed to resolve {domain}"


@register_command("open browser at {url}")
def open_browser(url: str):
    import webbrowser

    try:
        webbrowser.open(url)
        return f"🌐 Opened browser at: {url}"
    except Exception as e:
        return f"❌ Failed to open browser: {e}"
