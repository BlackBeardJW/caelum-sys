"""
Comprehensive tests for CaelumSys core functionality.

This module tests the main command processing system, plugin loading,
and registry functionality to ensure reliability across different
environments and Python versions.
"""

import pytest
import tempfile
import os
from unittest.mock import patch, MagicMock, mock_open
from caelum_sys.core_actions import do, extract_arguments_from_user_input, find_matching_command_template
from caelum_sys.registry import registry, register_command, get_registered_command_phrases
from caelum_sys import __version__

class TestCoreActions:
    """Test the main command processing system."""
    
    def test_do_function_exists(self):
        """Test that the main do() function is callable."""
        assert callable(do)
    
    def test_safe_commands_work(self):
        """Test that safe informational commands work without errors."""
        safe_commands = [
            "say hello",
            "get current time", 
            "get system info",
            "get python version"
        ]
        
        for command in safe_commands:
            try:
                result = do(command)
                assert isinstance(result, str)
                assert len(result) > 0
            except Exception as e:
                pytest.fail(f"Safe command '{command}' failed: {e}")
    
    def test_unknown_command_handling(self):
        """Test that unknown commands are handled gracefully."""
        result = do("this is definitely not a real command")
        assert "Unknown command" in result or "not found" in result.lower() or "No matching" in result
    
    def test_parameter_extraction(self):
        """Test argument extraction from user input."""
        # Test simple parameter extraction
        result = extract_arguments_from_user_input("ping google.com", "ping {host}")
        assert result == {"host": "google.com"}
        
        # Test multiple parameters
        result = extract_arguments_from_user_input(
            "copy file.txt to backup.txt", 
            "copy {source} to {destination}"
        )
        assert result == {"source": "file.txt", "destination": "backup.txt"}
    
    def test_fuzzy_matching(self):
        """Test that fuzzy matching works for typos."""
        # This should find "say hello" even with typos
        template = find_matching_command_template("say helo")
        assert template is not None

class TestRegistry:
    """Test the command registry system."""
    
    def test_registry_not_empty(self):
        """Test that commands are registered."""
        assert len(registry) > 0
        
    def test_get_command_phrases(self):
        """Test that we can get all registered command phrases."""
        phrases = get_registered_command_phrases()
        assert isinstance(phrases, list)
        assert len(phrases) > 0
        
    def test_register_command_decorator(self):
        """Test that the register_command decorator works."""
        initial_count = len(registry)
        
        @register_command("test command for testing")
        def test_func():
            return "test result"
        
        assert len(registry) == initial_count + 1
        assert "test command for testing" in registry
        assert registry["test command for testing"]["func"] == test_func

class TestPluginLoading:
    """Test that plugins load correctly."""
    
    def test_plugins_loaded(self):
        """Test that plugin commands are available."""
        expected_plugins = [
            "get current time",  # misc_commands
            "get my ip address", # network_tools 
            "take screenshot",   # screenshot_tools
            "get cpu usage",     # process_tools
        ]
        
        available_commands = get_registered_command_phrases()
        
        for plugin_command in expected_plugins:
            assert plugin_command in available_commands, f"Plugin command '{plugin_command}' not loaded"

class TestSafetyFeatures:
    """Test safety features and command classification."""
    
    def test_safe_commands_marked_correctly(self):
        """Test that safe commands are properly marked."""
        safe_commands = [
            "say hello",
            "get current time",
            "get system info",
            "take screenshot"
        ]
        
        for command in safe_commands:
            if command in registry:
                assert registry[command]["safe"] == True, f"Command '{command}' should be marked as safe"
    
    def test_unsafe_commands_marked_correctly(self):
        """Test that potentially dangerous commands are marked unsafe."""
        # Note: Some commands might not exist in current implementation
        potentially_unsafe = [
            "kill process by name test",  # process termination
            "lock screen",                # system state change
            "shut down in 5 minutes"     # system shutdown
        ]
        
        for command in potentially_unsafe:
            if command in registry:
                assert registry[command]["safe"] == False, f"Command '{command}' should be marked as unsafe"

class TestCommandExecution:
    """Test actual command execution with mocking."""
    
    @patch('platform.uname')
    def test_system_info_command(self, mock_uname):
        """Test system info command execution."""
        # Mock platform.uname() response
        mock_uname.return_value = MagicMock(
            system="TestOS", 
            node="TestNode",
            release="1.0",
            version="Test Version",
            machine="TestMachine",
            processor="TestProcessor"
        )
        
        result = do("get system info")
        assert "TestOS" in result
        assert "TestNode" in result
    
    def test_hello_command(self):
        """Test simple hello command."""
        result = do("say hello")
        assert "Hello" in result
        assert "Caelum" in result

class TestErrorHandling:
    """Test error handling and edge cases."""
    
    def test_empty_command(self):
        """Test handling of empty commands."""
        result = do("")
        assert isinstance(result, str)
        # Should handle gracefully, not crash
    
    def test_whitespace_command(self):
        """Test handling of whitespace-only commands."""
        result = do("   ")
        assert isinstance(result, str)
    
    def test_very_long_command(self):
        """Test handling of unusually long commands."""
        long_command = "x" * 1000
        result = do(long_command)
        assert isinstance(result, str)
        # Should not crash

class TestPackageMetadata:
    """Test package metadata and imports."""
    
    def test_version_available(self):
        """Test that package version is available."""
        # This might fail if __version__ isn't defined
        try:
            assert isinstance(__version__, str)
            assert len(__version__) > 0
        except (ImportError, AttributeError):
            pytest.skip("Package version not defined")
    
    def test_main_imports(self):
        """Test that main package components can be imported."""
        import caelum_sys
        from caelum_sys import core_actions
        from caelum_sys import registry
        
        # Basic smoke test - if we get here, imports worked
        assert hasattr(core_actions, 'do')
        assert hasattr(registry, 'register_command')

if __name__ == "__main__":
    pytest.main([__file__])
