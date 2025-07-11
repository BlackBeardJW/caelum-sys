from caelum_sys.registry import register_command
import pyautogui
import os

@register_command("pause music")
def pause_music():
    pyautogui.press("playpause")
    return "⏸️ Toggled play/pause."

@register_command("mute volume")
def mute_volume():
    pyautogui.press("volumemute")
    os.system("nircmd mutesysvolume toggle")  # Toggle mute using nircmd
    return "🔇 Volume muted/unmuted."

@register_command("volume up")
def volume_up():
    pyautogui.press("volumeup")
    return "🔊 Volume increased."

@register_command("volume down")
def volume_down():
    pyautogui.press("volumedown")
    return "🔉 Volume decreased."

@register_command("next track")
def next_track():
    pyautogui.press("nexttrack")
    return "⏭️ Skipped to next track."

@register_command("previous track")
def previous_track():
    pyautogui.press("prevtrack")
    return "⏮️ Went to previous track."

@register_command("open media player")
def open_media_player():
    pyautogui.press("playpause")  # or replace with subprocess to open app
    return "🎵 Media player toggled (or opened if already running)."
