# CaelumSys Installation and Usage Guide

## Installation

### Option 1: Install from PyPI
```bash
pip install caelum-sys
```

### Option 2: Install from source 
```bash
git clone https://github.com/BlackBeardJW/caelum-sys.git
cd caelum-sys
pip install -e .
```

### Option 3: Install dependencies manually
```bash
pip install psutil pyautogui requests pillow
```

## Basic Usage

### Simple Import and Execute
```python
from caelum_sys import do

# Execute any command
result = do("get current time")
print(result)  # ⏰ Current time: 2025-07-11 14:55:36

result = do("mute volume")
print(result)  # 🔇 Volume muted/unmuted.

result = do("create file at my_file.txt")
print(result)  # ✅ Created file at: my_file.txt
```

### List Available Commands
```python
from caelum_sys import do, get_registered_command_phrases

# Get all available commands
commands = get_registered_command_phrases()
print(f"Available commands: {len(commands)}")

for cmd in sorted(commands):
    print(f"  • {cmd}")
```

### Interactive Usage
```python
from caelum_sys import do

def interactive_mode():
    print("🤖 CaelumSys Interactive Mode")
    while True:
        user_input = input("Command: ").strip()
        if user_input.lower() in ["exit", "quit"]:
            break
        
        try:
            result = do(user_input)
            print(f"Result: {result}")
        except Exception as e:
            print(f"Error: {e}")

interactive_mode()
```

## Available Command Categories

### 📁 File Management
- `create file at example.txt`
- `delete file at example.txt`
- `copy file source.txt to dest.txt`
- `move file old.txt to new.txt`
- `create directory at my_folder`
- `list files in .`

### 🎵 Media Controls
- `mute volume`
- `volume up` / `volume down`
- `pause music`
- `next track` / `previous track`

### 🖥️ System Information
- `get system info`
- `get current time`
- `get cpu usage`
- `get memory usage`
- `get my ip address`

### 📸 Screenshots
- `take screenshot`
- `take screenshot with delay`
- `take screenshot with region`

### ⚙️ Process Management
- `list running processes`
- `kill process by name notepad`

### 🔧 Windows Tools
- `open task manager`
- `open file explorer`
- `lock workstation`

And many more! Use `get_registered_command_phrases()` to see all available commands.

## Error Handling

```python
from caelum_sys import do

try:
    result = do("invalid command")
    print(result)
except Exception as e:
    print(f"Command failed: {e}")
```

## Integration with AI/LLM

```python
from caelum_sys import do

def ai_system_control(natural_language_input):
    """
    This function can be called by an AI agent to control the system
    """
    try:
        result = do(natural_language_input)
        return f"Success: {result}"
    except Exception as e:
        return f"Error: {e}"

# Example usage by AI
ai_response = ai_system_control("take a screenshot")
print(ai_response)
```

## Requirements

- Python 3.7+
- Windows (currently - some commands are Windows-specific)
- Dependencies: psutil, pyautogui, requests, pillow

## Notes

- All plugins are automatically loaded when you import the package
- Commands are case-insensitive
- File paths can be relative or absolute
- Some commands may require elevated permissions
- All code is extensively documented with inline comments explaining functionality
- Each plugin module contains detailed docstrings explaining how commands work
- Function signatures and parameter types are clearly documented for developers
