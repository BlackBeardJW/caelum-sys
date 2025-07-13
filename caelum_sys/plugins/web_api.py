"""
Web and API operations plugin for internet connectivity and data retrieval.
"""

from caelum_sys.registry import register_command
import requests
import webbrowser
from urllib.parse import quote_plus
import json

@register_command("search web for {query}", safe=True)
def search_web(query: str):
    """Open a web search for the given query."""
    try:
        search_url = f"https://www.google.com/search?q={quote_plus(query)}"
        webbrowser.open(search_url)
        return f"🔍 Opened web search for: {query}"
    except Exception as e:
        return f"❌ Failed to open web search: {e}"

@register_command("check website status {url}", safe=True)
def check_website_status(url: str):
    """Check if a website is accessible."""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
        
        response = requests.get(url, timeout=10)
        status_code = response.status_code
        
        if status_code == 200:
            return f"✅ {url} is accessible (Status: {status_code})"
        else:
            return f"⚠️ {url} returned status code: {status_code}"
    except requests.exceptions.RequestException as e:
        return f"❌ Failed to reach {url}: {e}"

@register_command("get page title from {url}", safe=True)
def get_page_title(url: str):
    """Get the title of a web page."""
    try:
        if not url.startswith(('http://', 'https://')):
            url = 'https://' + url
            
        response = requests.get(url, timeout=10)
        
        # Simple title extraction
        content = response.text
        start = content.find('<title>') + 7
        end = content.find('</title>')
        
        if start > 6 and end > start:
            title = content[start:end].strip()
            return f"📄 Page title: {title}"
        else:
            return f"❌ Could not find title for {url}"
    except Exception as e:
        return f"❌ Failed to get page title: {e}"

@register_command("download file from {url}", safe=False)
def download_file(url: str, filename: str | None = None):
    """Download a file from the given URL."""
    try:
        if not filename:
            filename = url.split('/')[-1] or 'downloaded_file'
            
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        
        with open(filename, 'wb') as f:
            f.write(response.content)
            
        return f"⬇️ Downloaded file: {filename} ({len(response.content)} bytes)"
    except Exception as e:
        return f"❌ Failed to download file: {e}"

@register_command("shorten url {url}", safe=True)
def shorten_url(url: str):
    """Create a shortened version of a URL using TinyURL."""
    try:
        api_url = f"http://tinyurl.com/api-create.php?url={quote_plus(url)}"
        response = requests.get(api_url, timeout=10)
        
        if response.status_code == 200:
            short_url = response.text.strip()
            return f"🔗 Shortened URL: {short_url}"
        else:
            return f"❌ Failed to shorten URL"
    except Exception as e:
        return f"❌ Failed to shorten URL: {e}"

@register_command("get my public ip", safe=True)
def get_public_ip():
    """Get the public IP address."""
    try:
        response = requests.get('https://api.ipify.org', timeout=10)
        ip = response.text.strip()
        return f"🌐 Public IP address: {ip}"
    except Exception as e:
        return f"❌ Failed to get public IP: {e}"

@register_command("get weather for {city}", safe=True)
def get_weather(city: str):
    """Get basic weather information for a city."""
    try:
        # Using a free weather API (you might want to add API key support)
        url = f"http://wttr.in/{quote_plus(city)}?format=3"
        response = requests.get(url, timeout=10)
        weather = response.text.strip()
        return f"🌤️ Weather for {city}: {weather}"
    except Exception as e:
        return f"❌ Failed to get weather: {e}"
