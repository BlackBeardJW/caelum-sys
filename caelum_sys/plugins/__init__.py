# caelum_sys/plugins/__init__.py
"""
Plugin Loading System

This module handles the automatic discovery and loading of all CaelumSys plugins.
When load_plugins() is called, it scans the plugins directory and imports all
Python modules, which triggers their @register_command decorators to register
their commands with the system.

The plugin system is designed to be:
- Automatic: No manual registration needed
- Extensible: Just add a .py file to the plugins folder
- Isolated: Each plugin is a separate module
- Discoverable: All plugins are loaded at startup

Plugin Structure:
    Each plugin should be a Python file in this directory that uses the
    @register_command decorator to register its commands.
    
    Example plugin (example_plugin.py):
        from caelum_sys.registry import register_command
        
        @register_command("my command")
        def my_function():
            return "Command executed!"
"""

import importlib  # For dynamic module importing
import pkgutil    # For discovering modules in a package

def load_plugins():
    """
    Dynamically discover and import all plugin modules in the plugins package.
    
    This function scans the current package directory for all Python modules
    (excluding __init__.py and __pycache__) and imports them. When a plugin
    module is imported, any @register_command decorators in that module are
    executed, automatically registering the commands with the system.
    
    The loading process:
    1. Scan the plugins directory for .py files
    2. Import each module dynamically
    3. The import triggers @register_command decorators
    4. Commands become available in the global registry
    
    This function is automatically called when the main caelum_sys package
    is imported, so users don't need to call it manually.
    
    Example:
        # This happens automatically when you do:
        from caelum_sys import do
        
        # But you can also call it manually if needed:
        from caelum_sys.plugins import load_plugins
        load_plugins()
        
    Raises:
        ImportError: If a plugin module has syntax errors or missing dependencies
        
    Note:
        Failed plugin imports are currently not handled gracefully. Consider
        adding error handling for production use.
    """
    # Get the current package name (caelum_sys.plugins)
    package = __package__
    
    # Iterate through all modules in this package directory
    # pkgutil.iter_modules scans for .py files in __path__ (current directory)
    for _, module_name, _ in pkgutil.iter_modules(__path__):
        try:
            # Dynamically import the module
            # This triggers any @register_command decorators in the module
            full_module_name = f"{package}.{module_name}"
            importlib.import_module(full_module_name)
            
            # Optional: Print loading confirmation (can be disabled for cleaner output)
            # print(f"✅ Loaded plugin: {module_name}")
            
        except ImportError as e:
            # Handle cases where a plugin has missing dependencies or errors
            print(f"⚠️ Failed to load plugin '{module_name}': {e}")
            # Continue loading other plugins even if one fails
            continue
        except Exception as e:
            # Handle any other unexpected errors during plugin loading
            print(f"❌ Error loading plugin '{module_name}': {e}")
            continue

def get_plugin_info():
    """
    Get information about available plugins in the plugins directory.
    
    Returns:
        list: List of dictionaries containing plugin information
        
    Example:
        plugins = get_plugin_info()
        for plugin in plugins:
            print(f"Plugin: {plugin['name']}")
    """
    plugins = []
    
    for _, module_name, ispkg in pkgutil.iter_modules(__path__):
        if not ispkg:  # Only include modules, not sub-packages
            plugins.append({
                'name': module_name,
                'module_path': f"{__package__}.{module_name}",
                'is_package': ispkg
            })
    
    return plugins

def reload_plugins():
    """
    Reload all plugins by clearing the registry and loading them again.
    
    This is useful for development when you modify plugin code and want
    to reload the changes without restarting the Python interpreter.
    
    Warning:
        This will clear ALL registered commands and reload them from scratch.
        Use carefully in production environments.
    """
    # Import here to avoid circular imports
    from caelum_sys.registry import clear_registry
    
    # Clear all existing registered commands
    clear_registry()
    
    # Reload all plugins
    load_plugins()
    
    print("🔄 All plugins reloaded")
