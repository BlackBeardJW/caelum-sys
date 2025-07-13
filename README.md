# CaelumSys 🚀

![PyPI](https://img.shields.io/pypi/v/caelum-sys)
![Python Version](https://img.shields.io/pypi/pyversions/caelum-sys)
![Wheel](https://img.shields.io/pypi/wheel/caelum-sys)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)
![Downloads](https://img.shields.io/pypi/dm/caelum-sys)

**CaelumSys** is a comprehensive system automation toolkit that transforms natural language commands into system actions. With **117 commands across 20 specialized plugins**, it provides an intuitive interface for developers, scripters, and automation enthusiasts.

> ⚠️ **Early Development**: This project is in active development (v0.3.0). APIs may change between versions as we refine the interface and expand functionality.

---

## 🌟 Key Features

- **🗣️ Natural Language Interface**: `do("get current time")` instead of complex APIs
- **🔌 Plugin Architecture**: 20 specialized plugins covering daily automation needs  
- **🛡️ Safety Classifications**: Commands marked safe/unsafe for future AI agent integration
- **⚡ Zero Configuration**: Works immediately after `pip install caelum-sys`
- **🎯 117 Commands**: Comprehensive coverage from file operations to web APIs
- **🔧 Extensible**: Create custom plugins in just 10-15 lines of code
- **🌐 Cross-Platform**: Windows-focused with macOS/Linux compatibility

---

## 📦 Installation

```bash
pip install caelum-sys
```

**Development Installation:**
```bash
git clone https://github.com/BlackBeardJW/caelum-sys.git
cd caelum-sys
pip install -e .
```

---

## 🚀 Quick Start

### Python API
```python
from caelum_sys import do

# System Information
do("get current time")           # ⏰ Current time: 2025-07-13 15:30:45
do("get system info")            # 🖥️ System Info: Windows 11, Intel i7...
do("get cpu usage")              # 💻 CPU usage: 12.5%

# File Operations  
do("create file at report.txt")  # ✅ Created file at: report.txt
do("check if file exists data.json")  # ✅ File exists: data.json
do("get file size setup.py")     # 📏 File size: 1401 bytes (1.4 KB)

# Web & Network
do("check website status github.com")  # ✅ https://github.com is accessible (Status: 200)
do("get my public ip")           # 🌐 Public IP address: 203.0.113.42
do("get weather for London")     # 🌤️ Weather for London: ⛅ 18°C

# Text & Data Processing
do("encode base64 Hello World")  # 🔐 Encoded: SGVsbG8gV29ybGQ=
do("hash text with md5 secret")  # 🔒 MD5 hash: 5ebe2294ecd0e0f08eab7690d2a6ee69
do("generate uuid")              # 🆔 Generated UUID: 550e8400-e29b-41d4-a716...

# Productivity
do("add note Meeting at 3pm")    # 📝 Note saved with ID: 1
do("copy text to clipboard")     # 📋 Text copied to clipboard
do("calculate 15% of 240")       # 🧮 15% of 240 = 36.0

# Git Integration (for developers)
do("git status")                 # 📊 Git status: 3 modified files
do("git add all files")          # ✅ Added all files to staging
```

### Command Line Interface
```bash
# Get help and discover commands
caelum-sys "help"
caelum-sys "list safe commands"
caelum-sys "search commands for file"

# Execute commands
caelum-sys "get system info"
caelum-sys "take screenshot"
caelum-sys "check website status example.com"
```

---

## 📂 Plugin Categories

### 🗂️ **File Management** (8 commands)
Complete file system operations with safety checks.
```python
do("create folder Projects/my-app")      # Create directories
do("copy file data.txt to backup.txt")  # Copy operations  
do("move file temp.log to archive/")    # Move operations
do("delete file old-data.csv")          # Safe deletion
```

### 🌐 **Web & APIs** (7 commands)  
Internet connectivity and web service integration.
```python
do("check website status api.example.com")  # HTTP status checking
do("download file from https://...")        # File downloads
do("shorten url https://very-long-url...")  # URL shortening
do("get page title from news.ycombinator.com")  # Web scraping
```

### 📋 **Text & Clipboard** (8 commands)
Text manipulation and clipboard integration.
```python
do("copy text to clipboard")        # Clipboard operations
do("get clipboard content")         # Retrieve clipboard
do("uppercase text hello world")    # Text transformations
do("count words in text")          # Text analysis
```

### 🔢 **Math & Calculations** (7 commands)
Safe mathematical operations and unit conversions.
```python
do("calculate 15% of 240")                    # Percentage calculations
do("convert 100 fahrenheit to celsius")       # Temperature conversion
do("calculate tip 45.50 at 18 percent")      # Financial calculations
do("generate random number between 1 and 100")  # Random generation
```

### 📅 **Date & Time** (8 commands)
Temporal operations with timezone support.
```python
do("get current timestamp")              # Unix timestamps
do("add 5 days to today")               # Date arithmetic
do("what time is it in Tokyo")          # Timezone conversion
do("how many days until 2025-12-25")    # Date calculations
```

### 📝 **Quick Notes** (8 commands)
Persistent note management with JSON storage.
```python
do("save note Meeting with client tomorrow")  # Create notes
do("list all notes")                         # List notes
do("search notes for meeting")               # Search functionality
do("get note 1")                            # Retrieve specific notes
```

### 📊 **Git Integration** (12 commands)
Version control operations for developers.
```python
do("git status")                    # Repository status
do("git add all files")             # Stage changes
do("git commit with message Fix bug") # Commit changes
do("list git branches")             # Branch management
```

### ℹ️ **File Information** (7 commands)
Detailed file inspection and metadata.
```python
do("get file info document.pdf")              # Complete file details
do("get file hash important.zip")             # File integrity
do("find files with extension .py in src/")   # File discovery
do("count lines in file script.py")           # File analysis
```

### 🖥️ **System Utilities** (15+ commands)
System monitoring and control operations.
```python
do("get memory usage")           # Resource monitoring
do("list running processes")     # Process management  
do("take screenshot")           # Screen capture
do("open task manager")         # System tools
```

### 🔍 **Help & Discovery** (4 commands)
Built-in documentation and command discovery.
```python
do("help")                           # Complete command list
do("search commands for network")    # Find relevant commands
do("list safe commands")             # LLM-safe operations
do("list unsafe commands")           # Commands requiring permission
```

---

## 🤖 AI Agent Integration

CaelumSys is designed for future AI agent integration with built-in safety classifications:

### Safe Commands (102 total) ✅
Commands that **read information** without modifying system state:
```python
do("get current time")        # ✅ Safe - information retrieval
do("check website status")    # ✅ Safe - network checking  
do("get file size setup.py")  # ✅ Safe - file inspection
do("list running processes")  # ✅ Safe - system monitoring
```

### Unsafe Commands (15 total) ⚠️
Commands that **modify system state** and require explicit permission:
```python
do("delete file config.txt")  # ⚠️ Unsafe - file deletion
do("kill process chrome")     # ⚠️ Unsafe - process termination
do("empty recycle bin")       # ⚠️ Unsafe - system cleanup
do("git commit with message") # ⚠️ Unsafe - repository changes
```

**Query safe commands:** `do("list safe commands")`  
**Query unsafe commands:** `do("list unsafe commands")`

---

## 🛠️ Creating Custom Plugins

Extend CaelumSys with custom functionality:

```python
# caelum_sys/plugins/my_plugin.py
from caelum_sys.registry import register_command

@register_command("greet {name}", safe=True)
def greet_person(name: str):
    """Greet someone by name."""
    return f"👋 Hello, {name}! Welcome to CaelumSys!"

@register_command("backup database", safe=False)  
def backup_database():
    """Backup the application database."""
    # Implementation here
    return "💾 Database backup completed successfully"
```

**Plugin features:**
- ✅ **Auto-discovery**: Just add `.py` files to `caelum_sys/plugins/`
- ✅ **Parameter extraction**: `{name}` automatically becomes function parameter
- ✅ **Safety classification**: Mark commands as safe/unsafe for AI agents
- ✅ **Error handling**: Built-in exception handling and user-friendly messages

---

## 🧪 Development & Testing

```bash
# Install development dependencies
pip install -e ".[dev]"

# Run tests
pytest tests/

# Format code
black caelum_sys/
isort caelum_sys/

# Type checking
mypy caelum_sys/

# Build package
python -m build
```

**Project Structure:**
```
caelum_sys/
├── plugins/           # Plugin modules (16 total)
├── core_actions.py    # Main execution engine
├── registry.py        # Command registration system
├── cli.py            # Command-line interface
└── __init__.py       # Package interface
```

---

## 📋 Requirements

- **Python**: 3.9+ (tested on 3.9, 3.10, 3.11, 3.12, 3.13)
- **Operating System**: Windows (primary), macOS, Linux
- **Dependencies**: Automatically installed with package
  - `psutil` - System monitoring
  - `requests` - Web operations  
  - `pyperclip` - Clipboard integration
  - `pytz` - Timezone support
  - `python-dateutil` - Date parsing

---

## 🤝 Contributing

We welcome contributions! Here's how to get started:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-plugin`
3. **Add your plugin** to `caelum_sys/plugins/`
4. **Write tests** for your functionality
5. **Submit a pull request**

**Contribution Ideas:**
- 🔌 New plugins (email, database, cloud services)
- 📚 Documentation improvements
- 🧪 Additional test coverage
- 🐛 Bug fixes and optimizations
- 🌍 Cross-platform compatibility

---

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/caelum-sys/
- **GitHub Repository**: https://github.com/BlackBeardJW/caelum-sys
- **Issue Tracker**: https://github.com/BlackBeardJW/caelum-sys/issues
- **Documentation**: Coming soon!

---

## 📈 Roadmap

**v0.4.0 (Planned)**
- 🤖 Enhanced AI agent integration
- 📡 REST API server mode
- 🔧 Plugin management CLI
- 📚 Comprehensive documentation site

**v1.0.0 (Future)**
- 🎯 Stable API guarantee
- 🌐 Web dashboard interface
- 🔒 Advanced security features
- 📦 Plugin marketplace

---

<div align="center">

**Made with ❤️ by Joshua Wells**

⭐ **Star this repo** if you find CaelumSys useful!

</div>
