![PyPI](https://img.shields.io/pypi/v/caelum-sys)
![Wheel](https://img.shields.io/pypi/wheel/caelum-sys)
![Status](https://img.shields.io/pypi/status/caelum-sys)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

**caelum-sys** is a human-friendly system automation toolkit for Python.  
It allows natural language commands to control local system behavior — perfect for scripting, AI agents, or personal assistants like Caelum.

---

## Features

- Plugin-based architecture for easy command extension
- `do("open notepad")` style control
- Fully tested with `pytest`
- Built-in plugins: file ops, browser control, Spotify, system stats, screenshots
- Designed for LLM integration (text in, result out)

---

## Installation

        pip install caelum-sys

- Or for local development:

        git clone https://github.com/blackbeardjw/caelum-sys.git
        cd caelum-sys
        pip install -e .

## Usage
- Python:

        from caelum_sys import do

        do("open notepad")
        do("play spotify chill vibes")
        do("list files in Downloads")

- CLI:

        caelum-sys "get cpu usage"
        caelum-sys "open browser"

## Needs more Plugins

- The true power of caelum-sys lies in its plugin system. Each plugin you add unlocks new automation capabilities and natural language commands. Whether you're automating everyday tasks or building complex workflows, plugins make it possible. You're encouraged to contribute your own! Add any functionality you think would benefit the project and help push the limits of what caelum-sys can do.


## Adding Your Own Plugin
- Create a .py file in caelum_sys/plugins/ and use the decorator:

        from caelum_sys.registry import register_command

        @register_command("run my task")
        def my_command(command: str):
        return "Command executed!"

 ## Running Tests

 -   pytest tests

    All plugins are safely mocked (no system damage during testing).