# caelum_sys/plugins/__init__.py

import importlib
import pkgutil

def load_plugins():
    """
    Dynamically import all plugin modules in the plugins package.
    """
    package = __package__
    for _, name, _ in pkgutil.iter_modules(__path__):
        importlib.import_module(f"{package}.{name}")
