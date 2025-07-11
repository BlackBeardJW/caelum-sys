"""
CaelumSys Screenshot Tools Plugin

This plugin provides comprehensive screenshot capabilities including full-screen
captures, delayed screenshots, region-specific captures, and custom file naming.
All screenshot commands use pyautogui for cross-platform compatibility.

Commands provided:
- Basic Screenshots:
  * "take screenshot" - Capture entire screen, save as 'screenshot.png'
  * "take screenshot with delay" - Capture after specified delay (default 3s)
  
- Advanced Captures:
  * "take screenshot with region" - Capture specific screen area by coordinates
  * "take screenshot with custom filename" - Save with user-specified filename
  * "take screenshot with custom format" - Save in different format (jpg, bmp, etc.)

File Management:
- Screenshots are saved to the current working directory
- Default format is PNG for best quality
- Custom filenames should include file extension
- Supported formats: PNG, JPG, BMP, TIFF, and others supported by PIL

Dependencies:
- pyautogui: For screen capture functionality
- PIL (via pyautogui): For image processing and format support

Usage Examples:
    >>> from caelum_sys.core_actions import do
    >>> do("take screenshot")
    "📸 Screenshot saved as 'screenshot.png'."
    
    >>> do("take screenshot with delay")  # Uses default 3 second delay
    "📸 Screenshot taken after 3s delay. Saved as 'screenshot_delayed.png'."
    
    >>> do("take screenshot with custom filename my_capture.jpg")
    "📸 Screenshot saved as 'my_capture.jpg'."

All commands in this plugin are marked as safe=True since they only
capture screen content without modifying system state.
"""

from caelum_sys.registry import register_command
import pyautogui

@register_command("take screenshot")
def take_screenshot():
    """
    Take a full-screen screenshot and save as 'screenshot.png'.
    
    Captures the entire primary display and saves it in PNG format
    to the current working directory. This is the most basic and
    commonly used screenshot function.
    
    Returns:
        str: Confirmation message with filename
        
    Example:
        >>> take_screenshot()
        "📸 Screenshot saved as 'screenshot.png'."
        
    Note:
        - Captures primary display only in multi-monitor setups
        - Overwrites existing 'screenshot.png' file
        - PNG format provides best quality with lossless compression
    """
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    return "📸 Screenshot saved as 'screenshot.png'."

@register_command("take screenshot with delay")
def take_screenshot_with_delay(seconds: int = 3):
    """
    Take a screenshot after a specified delay period.
    
    This function waits for the specified number of seconds before
    capturing the screen. Useful for setting up the screen content
    or switching to the desired application before capture.
    
    Args:
        seconds (int): Delay in seconds before taking screenshot (default: 3)
        
    Returns:
        str: Confirmation message with delay time and filename
        
    Example:
        >>> take_screenshot_with_delay(5)
        "📸 Screenshot taken after 5s delay. Saved as 'screenshot_delayed.png'."
        
    Use Cases:
        - Switching to different applications before capture
        - Waiting for animations or loading to complete
        - Taking screenshots of temporary UI elements (menus, tooltips)
    """
    pyautogui.sleep(seconds)
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot_delayed.png")
    return f"📸 Screenshot taken after {seconds}s delay. Saved as 'screenshot_delayed.png'."

@register_command("take screenshot with region")
def take_screenshot_with_region(x: int = 100, y: int = 100, width: int = 300, height: int = 300):
    """
    Take a screenshot of a specific rectangular region of the screen.
    
    Captures only the specified area of the screen defined by the top-left
    corner coordinates (x, y) and the dimensions (width, height). Useful
    for capturing specific windows, UI elements, or areas of interest.
    
    Args:
        x (int): X-coordinate of top-left corner (default: 100)
        y (int): Y-coordinate of top-left corner (default: 100)
        width (int): Width of capture region in pixels (default: 300)
        height (int): Height of capture region in pixels (default: 300)
        
    Returns:
        str: Confirmation message with filename
        
    Example:
        >>> take_screenshot_with_region(0, 0, 800, 600)
        "📸 Region screenshot saved as 'screenshot_region.png'."
        
    Coordinate System:
        - (0, 0) is the top-left corner of the primary display
        - X increases rightward, Y increases downward
        - Coordinates outside screen bounds will be clipped
        
    Use Cases:
        - Capturing specific application windows
        - Documenting particular UI elements
        - Creating focused screenshots for tutorials
    """
    region = (x, y, width, height)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save("screenshot_region.png")
    return "📸 Region screenshot saved as 'screenshot_region.png'."

@register_command("take screenshot with custom filename")
def take_screenshot_with_custom_filename(filename: str = "custom_screenshot.png"):
    """
    Take a screenshot and save with a user-specified filename.
    
    Allows full control over the output filename and format by
    specifying the complete filename including extension. The file
    will be saved in the current working directory.
    
    Args:
        filename (str): Custom filename with extension (default: "custom_screenshot.png")
        
    Returns:
        str: Confirmation message with the specified filename
        
    Example:
        >>> take_screenshot_with_custom_filename("my_capture.jpg")
        "📸 Screenshot saved as 'my_capture.jpg'."
        
        >>> take_screenshot_with_custom_filename("desktop_2024-01-15.png")
        "📸 Screenshot saved as 'desktop_2024-01-15.png'."
        
    Supported Formats:
        - PNG: Lossless, best quality (recommended)
        - JPG/JPEG: Smaller file size, some quality loss
        - BMP: Uncompressed, large file size
        - TIFF: Lossless, supports metadata
        
    Note:
        - Include file extension in filename
        - Invalid extensions may cause save errors
        - Existing files will be overwritten
    """
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return f"📸 Screenshot saved as '{filename}'."

@register_command("take screenshot with custom format")
def take_screenshot_with_custom_format(format: str = "png"):
    """
    Take a screenshot and save in a specified image format.
    
    Captures a full-screen screenshot and saves it with the specified
    format extension. The filename will be 'screenshot_custom.[format]'.
    This is useful for quickly changing output format without specifying
    a full filename.
    
    Args:
        format (str): Image format extension (default: "png")
        
    Returns:
        str: Confirmation message with the generated filename
        
    Example:
        >>> take_screenshot_with_custom_format("jpg")
        "📸 Screenshot saved as 'screenshot_custom.jpg'."
        
        >>> take_screenshot_with_custom_format("bmp")
        "📸 Screenshot saved as 'screenshot_custom.bmp'."
        
    Supported Formats:
        - png: Best quality, lossless compression
        - jpg/jpeg: Good quality, smaller file size
        - bmp: Uncompressed, largest file size
        - tiff: Professional format, supports metadata
        - webp: Modern format, good compression
        
    Format Recommendations:
        - Use PNG for screenshots with text or UI elements
        - Use JPG for photographic content where file size matters
        - Use BMP for maximum compatibility with older software
    """
    filename = f"screenshot_custom.{format}"
    screenshot = pyautogui.screenshot()
    screenshot.save(filename)
    return f"📸 Screenshot saved as '{filename}'."
