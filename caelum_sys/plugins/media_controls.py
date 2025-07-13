"""
Media controls plugin for volume and playback control via keyboard shortcuts.
"""

from caelum_sys.registry import register_command
import pyautogui  # For sending keyboard shortcuts to control media
import os         # For executing system commands

@register_command("pause music")
def pause_music():
    """Toggle play/pause for the currently active media player."""
    pyautogui.press("playpause")
    return "⏸️ Toggled play/pause."

@register_command("mute volume")
def mute_volume():
    """Toggle system volume mute on/off."""
    pyautogui.press("volumemute")
    os.system("nircmd mutesysvolume toggle")  # Optional nircmd support
    return "🔇 Volume muted/unmuted."

@register_command("volume up")
def volume_up():
    """Increase the system volume by one step."""
    pyautogui.press("volumeup")
    return "🔊 Volume increased."

@register_command("volume down")
def volume_down():
    """Decrease the system volume by one step."""
    pyautogui.press("volumedown")
    return "🔉 Volume decreased."

@register_command("next track")
def next_track():
    """Skip to the next track in the currently playing media."""
    pyautogui.press("nexttrack")
    return "⏭️ Skipped to next track."

@register_command("previous track")
def previous_track():
    """Go back to the previous track in the currently playing media."""
    pyautogui.press("prevtrack")
    return "⏮️ Went to previous track."

@register_command("open media player")
def open_media_player():
    """Open or activate a media player."""
    pyautogui.press("playpause")
    return "🎵 Media player toggled (or opened if already running)."

# Additional utility functions for media control (not registered as commands)

def _check_media_keys_support():
    """Check if the system supports media keys."""
    try:
        return hasattr(pyautogui, 'press') and 'playpause' in pyautogui.KEYBOARD_KEYS
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
