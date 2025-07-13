"""
Text and clipboard operations plugin for content manipulation and transfer.
"""

from caelum_sys.registry import register_command
import pyperclip

@register_command("copy text to clipboard", safe=True)
def copy_to_clipboard(text: str):
    """Copy text to the system clipboard."""
    try:
        pyperclip.copy(text)
        return f"📋 Copied to clipboard: {text[:50]}{'...' if len(text) > 50 else ''}"
    except Exception as e:
        return f"❌ Failed to copy to clipboard: {e}"

@register_command("get clipboard content", safe=True)
def get_clipboard():
    """Get current clipboard content."""
    try:
        content = pyperclip.paste()
        if not content:
            return "📋 Clipboard is empty"
        return f"📋 Clipboard content: {content}"
    except Exception as e:
        return f"❌ Failed to get clipboard content: {e}"

@register_command("clear clipboard", safe=True)
def clear_clipboard():
    """Clear the clipboard content."""
    try:
        pyperclip.copy("")
        return "📋 Clipboard cleared"
    except Exception as e:
        return f"❌ Failed to clear clipboard: {e}"

@register_command("append to clipboard", safe=True)
def append_to_clipboard(text: str):
    """Append text to current clipboard content."""
    try:
        current = pyperclip.paste()
        new_content = current + text if current else text
        pyperclip.copy(new_content)
        return f"📋 Appended to clipboard: {text[:30]}{'...' if len(text) > 30 else ''}"
    except Exception as e:
        return f"❌ Failed to append to clipboard: {e}"

@register_command("count words in text", safe=True)
def count_words(text: str):
    """Count words in the given text."""
    word_count = len(text.split())
    char_count = len(text)
    return f"📊 Text statistics: {word_count} words, {char_count} characters"

@register_command("reverse text", safe=True)
def reverse_text(text: str):
    """Reverse the given text."""
    reversed_text = text[::-1]
    return f"🔄 Reversed text: {reversed_text}"

@register_command("uppercase text", safe=True)
def uppercase_text(text: str):
    """Convert text to uppercase."""
    return f"🔤 Uppercase: {text.upper()}"

@register_command("lowercase text", safe=True)
def lowercase_text(text: str):
    """Convert text to lowercase."""
    return f"🔤 Lowercase: {text.lower()}"
