#!/usr/bin/env python3
"""
CaelumSys v0.3.0 - Example Usage Demo (Early Development)

This script demonstrates the key features and commands available in CaelumSys.
Run this to see the system in action and explore what's possible.

Note: This project is in early development. Features may change between versions.
"""

from caelum_sys import do
import time

def demo_section(title, commands):
    """Run a demo section with a title and list of commands."""
    print(f"\n{'='*60}")
    print(f"📦 {title}")
    print('='*60)
    
    for cmd in commands:
        print(f"\n🚀 Executing: do('{cmd}')")
        try:
            result = do(cmd)
            print(f"✅ Result: {result}")
        except Exception as e:
            print(f"❌ Error: {e}")
        time.sleep(1)  # Small delay for readability

def main():
    """Run the CaelumSys demo."""
    print("🎉 Welcome to CaelumSys v0.3.0 Demo! (Early Development)")
    print("This demo showcases the 117+ commands across 16 plugins")
    
    # Basic System Info
    demo_section("Basic System Information", [
        "get current time",
        "get system info", 
        "get my public ip",
        "get cpu usage"
    ])
    
    # File Operations
    demo_section("File Operations", [
        "check if file exists setup.py",
        "get file size setup.py",
        "get file info setup.py"
    ])
    
    # Web Operations  
    demo_section("Web & API Operations", [
        "check website status github.com",
        "get page title from github.com"
    ])
    
    # Text & Data Processing
    demo_section("Text & Data Processing", [
        "encode base64 Hello World",
        "generate uuid",
        "hash text with md5 password123"
    ])
    
    # Math & Calculations
    demo_section("Math & Calculations", [
        "calculate 15% of 240", 
        "convert 100 fahrenheit to celsius",
        "calculate square root of 144"
    ])
    
    # Date & Time
    demo_section("Date & Time Operations", [
        "get current timestamp",
        "add 5 days to today"
    ])
    
    # Help System
    demo_section("Help & Discovery", [
        "search commands for file",
        "list safe commands"
    ])
    
    print(f"\n{'='*60}")
    print("🎯 Demo Complete!")
    print("✨ You've seen just a sample of CaelumSys' 117+ commands")
    print("🔍 Run do('help') to see all available commands")
    print("📚 Check the README.md for complete documentation")
    print('='*60)

if __name__ == "__main__":
    main()
