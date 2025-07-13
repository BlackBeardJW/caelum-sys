"""
Media controls plugin for volume and playback control via keyboard shortcuts.
"""

import os  # For executing system commands

try:
    # Only try to import pyautogui if we're in a GUI environment or can safely handle headless
    if (
        os.environ.get("DISPLAY")
        or os.name == "nt"
        or os.environ.get("PYTEST_CURRENT_TEST")
    ):
        import pyautogui  # For sending keyboard shortcuts to control media
    else:
        # Try importing anyway but catch any display-related errors
        import pyautogui  # For sending keyboard shortcuts to control media
    MEDIA_CONTROLS_AVAILABLE = True
except (ImportError, Exception):
    # Catch both import errors and any display-related exceptions
    pyautogui = None  # type: ignore
    MEDIA_CONTROLS_AVAILABLE = False

from caelum_sys.registry import register_command


@register_command("pause music")
def pause_music():
    """Toggle play/pause for the currently active media player."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("playpause")
        return "⏸️ Toggled play/pause."
    except Exception as e:
        return f"❌ Failed to control media: {e}"


@register_command("mute volume")
def mute_volume():
    """Toggle system volume mute on/off."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("volumemute")
        os.system("nircmd mutesysvolume toggle")  # Optional nircmd support
        return "🔇 Volume muted/unmuted."
    except Exception as e:
        return f"❌ Failed to control volume: {e}"


@register_command("volume up")
def volume_up():
    """Increase the system volume by one step."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("volumeup")
        return "🔊 Volume increased."
    except Exception as e:
        return f"❌ Failed to increase volume: {e}"


@register_command("volume down")
def volume_down():
    """Decrease the system volume by one step."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("volumedown")
        return "🔉 Volume decreased."
    except Exception as e:
        return f"❌ Failed to decrease volume: {e}"


@register_command("next track")
def next_track():
    """Skip to the next track in the currently playing media."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("nexttrack")
        return "⏭️ Skipped to next track."
    except Exception as e:
        return f"❌ Failed to skip track: {e}"


@register_command("previous track")
def previous_track():
    """Go back to the previous track in the currently playing media."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("prevtrack")
        return "⏮️ Went to previous track."
    except Exception as e:
        return f"❌ Failed to go to previous track: {e}"


@register_command("open media player")
def open_media_player():
    """Open or activate a media player."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return "❌ Media controls not available on this system"
    try:
        pyautogui.press("playpause")
        return "🎵 Media player toggled (or opened if already running)."
    except Exception as e:
        return f"❌ Failed to open media player: {e}"


# Additional utility functions for media control (not registered as commands)


def _check_media_keys_support():
    """Check if the system supports media keys."""
    if not MEDIA_CONTROLS_AVAILABLE or pyautogui is None:
        return False
    try:
        return hasattr(pyautogui, "press") and "playpause" in pyautogui.KEYBOARD_KEYS
    except:
        return False


def _get_media_control_help():
    """Get help text for media control commands."""
    help_text = """
    Media Control Commands:
    =====================
    
    Volume Control:
    - "mute volume" - Toggle system mute on/off
    - "volume up" - Increase volume one step
    - "volume down" - Decrease volume one step
    
    Playback Control:
    - "pause music" - Toggle play/pause
    - "next track" - Skip to next song
    - "previous track" - Go to previous song
    - "open media player" - Open/toggle media player
    
    Note: These commands work with most media players and the system
    volume controls. Results may vary depending on your specific setup.
    """
    return help_text
