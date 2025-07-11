import pytest
from unittest.mock import patch, MagicMock
from caelum_sys.core_actions import do

# --- FILES PLUGIN ---
@patch("caelum_sys.plugins.files.os.listdir", return_value=["file1.txt", "file2.md"])
def test_list_files(mock_listdir):
    result = do("list files in .")
    assert "file1.txt" in result

@patch("caelum_sys.plugins.files.os.remove")
def test_delete_file(mock_remove):
    result = do("delete file test.txt")
    assert "Deleted" in result

@patch("caelum_sys.plugins.files.open")
def test_create_file(mock_open):
    result = do("create file temp.txt")
    assert "Created empty file" in result

# --- SPOTIFY PLUGIN ---
def test_play_spotify():
    result = do("play spotify lofi chill")
    assert "lofi chill" in result

# --- BROWSER PLUGIN ---
@patch("caelum_sys.plugins.browser.webbrowser.open")
def test_open_browser(mock_open):
    result = do("open browser")
    assert "Opening browser" in result

@patch("caelum_sys.plugins.browser.webbrowser.open")
def test_open_url(mock_open):
    result = do("open url example.com")
    assert "example.com" in result

# --- SYSTEM INFO PLUGIN ---
@patch("caelum_sys.plugins.system_info.psutil.cpu_percent", return_value=42)
def test_cpu_usage(mock_cpu):
    result = do("get cpu usage")
    assert "42" in result

@patch("caelum_sys.plugins.system_info.psutil.virtual_memory")
def test_memory_stats(mock_mem):
    mock_mem.return_value = MagicMock(
        used=2 * 1024**3,  # 2GB
        total=8 * 1024**3, # 8GB
        percent=25
    )
    result = do("get memory stats")
    assert "25%" in result

# --- SCREENSHOT PLUGIN ---
@patch("caelum_sys.plugins.screenshot.pyautogui.screenshot")
@patch("caelum_sys.plugins.screenshot.os.makedirs")
def test_screenshot(mock_makedirs, mock_screenshot):
    result = do("take screenshot")
    assert "Screenshot saved to" in result
