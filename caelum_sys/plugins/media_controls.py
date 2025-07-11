"""
Media Controls Plugin

This plugin provides commands for controlling media playback and system audio.
It uses pyautogui to send keyboard shortcuts that most media players and the
operating system recognize for volume and playback control.

Commands provided:
- "mute volume" - Toggle system volume mute
- "volume up" - Increase system volume  
- "volume down" - Decrease system volume
- "pause music" - Toggle play/pause for media
- "next track" - Skip to next track
- "previous track" - Go to previous track
- "open media player" - Toggle media player (or send play/pause)

Dependencies:
- pyautogui: For sending keyboard shortcuts
- os: For system commands (optional nircmd integration)

Note:
The volume mute function attempts to use 'nircmd' (NirCmd utility) for
additional volume control, but will work with just pyautogui if nircmd
is not installed.
"""

from caelum_sys.registry import register_command
import pyautogui  # For sending keyboard shortcuts to control media
import os         # For executing system commands

@register_command("pause music")
def pause_music():
    """
    Toggle play/pause for the currently active media player.
    
    This command sends the "playpause" key which is recognized by most
    media players (Spotify, iTunes, Windows Media Player, VLC, etc.)
    and will toggle between play and pause states.
    
    Returns:
        str: Success message indicating the action was performed
        
    Example:
        result = do("pause music")
        # Result: "⏸️ Toggled play/pause."
    """
    # Send the media play/pause key
    # This is a standard media key that most applications recognize
    pyautogui.press("playpause")
    return "⏸️ Toggled play/pause."

@register_command("mute volume")
def mute_volume():
    """
    Toggle system volume mute on/off.
    
    This command attempts two methods for muting volume:
    1. Sends the "volumemute" key via pyautogui (standard approach)
    2. Tries to use nircmd utility for additional control (if available)
    
    The nircmd command is optional and will fail silently if the utility
    is not installed on the system.
    
    Returns:
        str: Success message indicating volume was muted/unmuted
        
    Example:
        result = do("mute volume")
        # Result: "🔇 Volume muted/unmuted."
        
    Note:
        You may see an error about 'nircmd' not being recognized - this is
        normal if you don't have NirCmd installed and doesn't affect the
        primary volume mute functionality.
    """
    # Method 1: Use the standard volume mute key
    pyautogui.press("volumemute")
    
    # Method 2: Try to use nircmd for additional volume control (optional)
    # nircmd is a third-party utility that provides advanced system control
    # If it's not installed, this command will fail but won't break the function
    os.system("nircmd mutesysvolume toggle")  # Toggle mute using nircmd
    
    return "🔇 Volume muted/unmuted."

@register_command("volume up")
def volume_up():
    """
    Increase the system volume by one step.
    
    Sends the "volumeup" key which is handled by the operating system
    to increase the volume level. The amount of increase depends on
    the system's volume step settings.
    
    Returns:
        str: Success message indicating volume was increased
        
    Example:
        result = do("volume up")
        # Result: "🔊 Volume increased."
    """
    # Send the volume up key
    pyautogui.press("volumeup")
    return "🔊 Volume increased."

@register_command("volume down")
def volume_down():
    """
    Decrease the system volume by one step.
    
    Sends the "volumedown" key which is handled by the operating system
    to decrease the volume level. The amount of decrease depends on
    the system's volume step settings.
    
    Returns:
        str: Success message indicating volume was decreased
        
    Example:
        result = do("volume down")
        # Result: "🔉 Volume decreased."
    """
    # Send the volume down key
    pyautogui.press("volumedown")
    return "🔉 Volume decreased."

@register_command("next track")
def next_track():
    """
    Skip to the next track in the currently playing media.
    
    Sends the "nexttrack" media key which is recognized by most media
    players to advance to the next song/track in the playlist or queue.
    
    Returns:
        str: Success message indicating track was skipped
        
    Example:
        result = do("next track")
        # Result: "⏭️ Skipped to next track."
    """
    # Send the next track media key
    pyautogui.press("nexttrack")
    return "⏭️ Skipped to next track."

@register_command("previous track")
def previous_track():
    """
    Go back to the previous track in the currently playing media.
    
    Sends the "prevtrack" media key which is recognized by most media
    players to go back to the previous song/track in the playlist or queue.
    
    Returns:
        str: Success message indicating track was changed
        
    Example:
        result = do("previous track")
        # Result: "⏮️ Went to previous track."
    """
    # Send the previous track media key
    pyautogui.press("prevtrack")
    return "⏮️ Went to previous track."

@register_command("open media player")
def open_media_player():
    """
    Attempt to open or activate a media player.
    
    This command sends a play/pause key, which typically has the behavior
    of opening the default media player if no player is currently active,
    or toggling play/pause if a player is already running.
    
    The exact behavior depends on the system configuration and which
    media players are installed.
    
    Returns:
        str: Success message indicating the action was performed
        
    Example:
        result = do("open media player")
        # Result: "🎵 Media player toggled (or opened if already running)."
        
    Note:
        This is a best-effort command. If you need to open a specific
        media player, consider using the "open app" commands instead.
    """
    # Send play/pause key - this often opens media player if none is active
    pyautogui.press("playpause")
    return "🎵 Media player toggled (or opened if already running)."

# Additional utility functions for media control (not registered as commands)

def _check_media_keys_support():
    """
    Check if the system supports media keys.
    
    This is a private utility function (note the underscore prefix) that
    could be used to verify media key support before executing commands.
    
    Returns:
        bool: True if media keys are likely supported, False otherwise
        
    Note:
        This is a placeholder function. Actual implementation would need
        to test the system's capability to handle media keys.
    """
    # This is a simplified check - in practice, you might want to test
    # if pyautogui can successfully send media keys
    try:
        # Test if pyautogui has the required key mappings
        return hasattr(pyautogui, 'press') and 'playpause' in pyautogui.KEYBOARD_KEYS
    except:
        return False

def _get_media_control_help():
    """
    Get help text for media control commands.
    
    Returns:
        str: Formatted help text explaining available media commands
    """
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
