import webbrowser
from caelum_sys.registry import register_command

@register_command("open browser")
def open_browser(command: str):
    try:
        webbrowser.open("https://google.com")
        return "🌐 Opening browser to google.com"
    except Exception as e:
        return f"❌ Failed to open browser: {e}"

@register_command("open url")
def open_url(command: str):
    url = command[len("open url"):].strip()
    try:
        if not url.startswith("http"):
            url = "https://" + url
        webbrowser.open(url)
        return f"🌐 Opening {url}"
    except Exception as e:
        return f"❌ Could not open URL: {e}"
