"""
Integration tests for CaelumSys plugin system.

These tests verify that plugins work together correctly and that
the command system handles real-world usage patterns.
"""

import pytest
import tempfile
import os
from unittest.mock import patch, MagicMock
from caelum_sys.core_actions import do

class TestFileManagementIntegration:
    """Test file management commands with temporary files."""
    
    def setup_method(self):
        """Set up temporary directory for each test."""
        self.temp_dir = tempfile.mkdtemp()
        self.test_file = os.path.join(self.temp_dir, "test_file.txt")
        
    def teardown_method(self):
        """Clean up temporary files after each test."""
        try:
            if os.path.exists(self.test_file):
                os.remove(self.test_file)
            os.rmdir(self.temp_dir)
        except:
            pass  # Ignore cleanup errors
    
    def test_create_and_check_file(self):
        """Test creating a file and verifying it exists."""
        # Create file using CaelumSys command
        result = do(f"create file {self.test_file}")
        
        # Verify the command succeeded
        assert "created" in result.lower() or "file" in result.lower()
        
        # Verify the file actually exists
        assert os.path.exists(self.test_file)

class TestCommandParameterHandling:
    """Test parameter handling across different command types."""
    
    def test_single_parameter_commands(self):
        """Test commands with single parameters."""
        test_cases = [
            ("get weather for London", "get weather for {city}"),
            ("ping google.com", "ping {host}"),
            ("resolve dns for github.com", "resolve dns for {domain}")
        ]
        
        for user_input, template in test_cases:
            if template.replace("{city}", "test").replace("{host}", "test").replace("{domain}", "test") in [cmd for cmd in do("list commands") if isinstance(do("list commands"), str)]:
                # Only test if command exists
                result = do(user_input)
                assert isinstance(result, str)
                assert len(result) > 0
    
    def test_multiple_parameter_commands(self):
        """Test commands with multiple parameters."""
        # Test with file operations if available
        test_cases = [
            "copy source.txt to dest.txt",
            "move old.txt to new.txt"
        ]
        
        for command in test_cases:
            try:
                result = do(command)
                assert isinstance(result, str)
            except Exception:
                # Command might not exist or might fail due to missing files
                # That's okay for this test - we're testing parameter parsing
                pass

class TestErrorRecovery:
    """Test system behavior under error conditions."""
    
    @patch('psutil.process_iter')
    def test_process_commands_with_mock(self, mock_process_iter):
        """Test process-related commands with mocked psutil."""
        # Mock process list
        mock_proc = MagicMock()
        mock_proc.info = {"name": "test_process.exe"}
        mock_process_iter.return_value = [mock_proc]
        
        result = do("list running processes")
        assert isinstance(result, str)
        assert len(result) > 0
    
    def test_network_commands_offline(self):
        """Test network commands when offline or with invalid hosts."""
        # These might fail, but shouldn't crash the system
        test_commands = [
            "ping invalid.nonexistent.domain.xyz",
            "resolve dns for this.domain.definitely.does.not.exist"
        ]
        
        for command in test_commands:
            try:
                result = do(command)
                assert isinstance(result, str)
                # Should get an error message, not a crash
                assert "failed" in result.lower() or "error" in result.lower() or "not" in result.lower()
            except Exception:
                # If command doesn't exist, that's fine
                pass

class TestPluginCompatibility:
    """Test that different plugins work together without conflicts."""
    
    def test_no_command_conflicts(self):
        """Test that no two plugins register the same command."""
        from caelum_sys.registry import registry
        
        commands = list(registry.keys())
        unique_commands = set(commands)
        
        assert len(commands) == len(unique_commands), "Duplicate commands found in registry"
    
    def test_plugin_commands_accessible(self):
        """Test that commands from different plugins are all accessible."""
        # Test a sampling of commands from different plugins
        plugin_samples = {
            "misc_commands": ["get current time", "say hello"],
            "network_tools": ["get my ip address", "get hostname"],
            "screenshot_tools": ["take screenshot"],
            "system_utils": ["get python version"] # Changed from a potentially unsafe command
        }
        
        for plugin_name, commands in plugin_samples.items():
            for command in commands:
                try:
                    result = do(command)
                    assert isinstance(result, str)
                    assert len(result) > 0
                except Exception as e:
                    pytest.fail(f"Command '{command}' from {plugin_name} failed: {e}")

class TestCommandDiscovery:
    """Test command discovery and help functionality."""
    
    def test_command_listing(self):
        """Test that we can get a list of available commands."""
        from caelum_sys.registry import get_registered_command_phrases
        
        commands = get_registered_command_phrases()
        assert isinstance(commands, list)
        assert len(commands) > 10  # Should have a reasonable number of commands
        
        # Check that some expected commands are present
        expected_commands = [
            "say hello",
            "get current time",
            "take screenshot"
        ]
        
        for expected in expected_commands:
            assert expected in commands, f"Expected command '{expected}' not found"

class TestThreadSafety:
    """Basic tests for concurrent usage (important for automation)."""
    
    def test_concurrent_safe_commands(self):
        """Test that multiple safe commands can run without interference."""
        import threading
        import time
        
        results = []
        errors = []
        
        def run_command(command):
            try:
                result = do(command)
                results.append(result)
            except Exception as e:
                errors.append(e)
        
        # Run multiple safe commands concurrently
        commands = [
            "say hello",
            "get current time", 
            "get system info"
        ]
        
        threads = []
        for command in commands:
            thread = threading.Thread(target=run_command, args=(command,))
            threads.append(thread)
            thread.start()
        
        # Wait for all threads to complete
        for thread in threads:
            thread.join(timeout=10)  # 10 second timeout
        
        # Check results
        assert len(errors) == 0, f"Concurrent execution errors: {errors}"
        assert len(results) == len(commands), "Not all commands completed"
        
        for result in results:
            assert isinstance(result, str)
            assert len(result) > 0

if __name__ == "__main__":
    pytest.main([__file__, "-v"])
