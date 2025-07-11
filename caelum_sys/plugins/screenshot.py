from caelum_sys.registry import register_command
import pyautogui
import os
from datetime import datetime

@register_command("take screenshot")
def take_screenshot(command: str):
    try:
        os.makedirs("screenshots", exist_ok=True)
        filename = datetime.now().strftime("screenshots/screen_%Y%m%d_%H%M%S.png")
        pyautogui.screenshot(filename)
        return f"📸 Screenshot saved to {filename}"
    except Exception as e:
        return f"❌ Screenshot failed: {e}"
