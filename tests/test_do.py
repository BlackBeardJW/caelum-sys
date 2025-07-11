import pytest
from unittest.mock import patch, MagicMock
from caelum_sys.core_actions import do

@patch("caelum_sys.system.subprocess.Popen")
def test_do_open_app(mock_popen):
    result = do("open notepad")
    assert "Opening notepad" in result
    mock_popen.assert_called_once()

@patch("caelum_sys.system.psutil.process_iter")
def test_do_kill_process(mock_iter):
    fake_proc = MagicMock()
    fake_proc.name.return_value = "discord"
    mock_iter.return_value = [fake_proc]

    result = do("kill discord")
    assert "Killed process" in result
    fake_proc.kill.assert_called_once()

@patch("caelum_sys.system.os.system")
def test_do_shutdown(mock_system):
    result = do("shutdown")
    assert "System is shutting down" in result
    mock_system.assert_called_once()