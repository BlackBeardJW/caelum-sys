# tests/test_plugins.py

import pytest
from caelum_sys.registry import get_safe_registry, registry, get_registered_command_phrases

test_args = {
    "path": "test_temp.txt",
    "source": "test_temp.txt",
    "destination": "test_temp_copy.txt",
    "directory": ".",
    "filename": "test_custom.png",
    "format": "png"
}

safe_registry = get_safe_registry()

@pytest.mark.parametrize("command", get_registered_command_phrases())
def test_plugin(command):
    func = registry[command]
    try:
        # Try calling without args to catch missing argument errors
        func()
    except TypeError:
        pass  # Expected if the function requires args
    except Exception as e:
        pytest.fail(f"Plugin '{command}' failed with error: {e}")
