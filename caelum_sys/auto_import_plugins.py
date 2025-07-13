import importlib
import os
import pathlib

def load_all_plugins():
    plugins_dir = pathlib.Path(__file__).parent / "plugins"

    for file in os.listdir(plugins_dir):
        if file.endswith(".py") and not file.startswith("__"):
            module_name = f"caelum_sys.plugins.{file[:-3]}"
            try:
                module = importlib.import_module(module_name)
                print(f"🔌 Loaded plugin: {module_name}")
                # Ensure the plugin is registered (if it has a register function)
                if hasattr(module, "register"):
                    module.register()
            except ImportError as e:
                print(f"⚠️ Failed to load plugin '{file[:-3]}': {e}")
