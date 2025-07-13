"""
Screenshot tools plugin for capturing screen content in various formats and regions.
"""

try:
    import pyautogui

    SCREENSHOT_AVAILABLE = True
except ImportError:
    pyautogui = None  # type: ignore
    SCREENSHOT_AVAILABLE = False

from caelum_sys.registry import register_command


@register_command("take screenshot")
def take_screenshot():
    """Take a full-screen screenshot and save as 'screenshot.png'."""
    if not SCREENSHOT_AVAILABLE or pyautogui is None:
        return "❌ Screenshot functionality not available on this system"
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot.png")
        return "📸 Screenshot saved as 'screenshot.png'."
    except Exception as e:
        return f"❌ Failed to take screenshot: {e}"


@register_command("take screenshot with delay")
def take_screenshot_with_delay(seconds: int = 3):
    """Take a screenshot after a specified delay."""
    if not SCREENSHOT_AVAILABLE or pyautogui is None:
        return "❌ Screenshot functionality not available on this system"
    try:
        pyautogui.sleep(seconds)
        screenshot = pyautogui.screenshot()
        screenshot.save("screenshot_delayed.png")
        return f"📸 Screenshot taken after {seconds}s delay. Saved as 'screenshot_delayed.png'."
    except Exception as e:
        return f"❌ Failed to take delayed screenshot: {e}"


@register_command("take screenshot with region")
def take_screenshot_with_region(
    x: int = 100, y: int = 100, width: int = 300, height: int = 300
):
    """Take a screenshot of a specific rectangular region."""
    if not SCREENSHOT_AVAILABLE or pyautogui is None:
        return "❌ Screenshot functionality not available on this system"
    try:
        region = (x, y, width, height)
        screenshot = pyautogui.screenshot(region=region)
        screenshot.save("screenshot_region.png")
        return "📸 Region screenshot saved as 'screenshot_region.png'."
    except Exception as e:
        return f"❌ Failed to take region screenshot: {e}"


@register_command("take screenshot with custom filename")
def take_screenshot_with_custom_filename(filename: str = "custom_screenshot.png"):
    """Take a screenshot with a user-specified filename."""
    if not SCREENSHOT_AVAILABLE or pyautogui is None:
        return "❌ Screenshot functionality not available on this system"
    try:
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        return f"📸 Screenshot saved as '{filename}'."
    except Exception as e:
        return f"❌ Failed to take screenshot: {e}"


@register_command("take screenshot with custom format")
def take_screenshot_with_custom_format(format: str = "png"):
    """Take a screenshot and save in specified format."""
    if not SCREENSHOT_AVAILABLE or pyautogui is None:
        return "❌ Screenshot functionality not available on this system"
    try:
        filename = f"screenshot_custom.{format}"
        screenshot = pyautogui.screenshot()
        screenshot.save(filename)
        return f"📸 Screenshot saved as '{filename}'."
    except Exception as e:
        return f"❌ Failed to take screenshot: {e}"
