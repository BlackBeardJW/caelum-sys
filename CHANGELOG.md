# Changelog

All notable changes to CaelumSys will be documented in this file.

## [0.3.0] - 2025-07-13

### 🚀 Major Release - Professional Package

**New Features:**
- **117 Commands** across 20 comprehensive plugins
- **Plugin Safety Classification** - Commands marked as `safe=True/False` for AI integration
- **Modern Package Structure** - Migrated from setup.py to pyproject.toml only
- **Professional Documentation** - Complete README with examples and usage guides
- **CI/CD Pipeline** - GitHub Actions for automated testing and releases
- **Automated PyPI Publishing** - Trusted publishing setup

**New Plugins Added:**
- **text_clipboard.py** - 8 clipboard and text manipulation commands
- **web_api.py** - 7 web requests, URL operations, and weather API
- **data_processing.py** - 11 JSON/CSV conversion, encoding, and hashing commands  
- **math_calculations.py** - 7 safe calculations and unit conversions
- **date_time.py** - 8 timezone, timestamp, and date calculation commands
- **quick_notes.py** - 8 note management commands with JSON persistence
- **git_integration.py** - 12 git operations for developers
- **file_info.py** - 7 file inspection and metadata commands
- **help_system.py** - 4 help and command discovery commands
- **dev_tools.py** - Development utilities and debugging commands
- **monitoring_tools.py** - System monitoring and performance tracking
- **caelum_control.py** - Core system control operations

**Enhanced Features:**
- **117 Total Commands** across 20 plugins
- **Automatic Plugin Discovery** - Just add .py files to plugins folder
- **Cross-Platform Compatibility** - Windows, macOS, Linux support
- **Zero Configuration Setup** - Works immediately after pip install

**Dependencies Added:**
- `python-dateutil` - Advanced date parsing
- `pyperclip` - Clipboard operations  
- `pytz` - Timezone support

**Documentation:**
- Updated README.md with comprehensive examples
- Added plugin categories and LLM integration guide
- Created detailed usage examples for all command types

**Developer Experience:**
- Plugin creation now takes only 10-15 lines
- Consistent error handling across all plugins
- Improved command pattern matching
- Better Unicode handling for Windows terminals

**LLM Integration Preparation:**
- Built-in safety classification system for future AI agent use
- Commands pre-categorized for eventual LLM integration
- Foundation for safe vs unsafe operation filtering

---

## [0.2.2] - Previous Release

### Features:
- Basic plugin system
- 39 original commands across 8 plugins
- File management, system controls, media operations
- CLI interface with `caelum-sys` command

### Plugins:
- file_management.py
- media_controls.py  
- misc_commands.py
- network_tools.py
- process_tools.py
- screenshot_tools.py
- system_utils.py
- windows_tools.py
