"""
File information plugin for inspecting file properties and metadata.
"""

import hashlib
import os
from datetime import datetime

from caelum_sys.registry import register_command


@register_command("get file size {path}", safe=True)
def get_file_size(path: str):
    """Get the size of a file in bytes and human-readable format."""
    try:
        if not os.path.exists(path):
            return f"❌ File not found: {path}"

        if os.path.isdir(path):
            return f"❌ {path} is a directory, not a file"

        size_bytes = os.path.getsize(path)

        # Convert to human readable format
        for unit in ["B", "KB", "MB", "GB"]:
            if size_bytes < 1024:
                size_human = f"{size_bytes:.1f} {unit}"
                break
            size_bytes /= 1024
        else:
            size_human = f"{size_bytes:.1f} TB"

        return f"📏 File size: {os.path.getsize(path)} bytes ({size_human})"
    except Exception as e:
        return f"❌ Error getting file size: {e}"


@register_command("check if file exists {path}", safe=True)
def check_file_exists(path: str):
    """Check if a file or directory exists."""
    try:
        if os.path.exists(path):
            if os.path.isfile(path):
                return f"✅ File exists: {path}"
            elif os.path.isdir(path):
                return f"✅ Directory exists: {path}"
            else:
                return f"✅ Path exists: {path} (special file type)"
        else:
            return f"❌ Path does not exist: {path}"
    except Exception as e:
        return f"❌ Error checking path: {e}"


@register_command("get file extension {path}", safe=True)
def get_file_extension(path: str):
    """Get the file extension from a file path."""
    try:
        _, extension = os.path.splitext(path)
        if extension:
            return f"📄 File extension: {extension}"
        else:
            return f"📄 No file extension found for: {path}"
    except Exception as e:
        return f"❌ Error getting extension: {e}"


@register_command("count lines in file {path}", safe=True)
def count_lines(path: str):
    """Count the number of lines in a text file."""
    try:
        if not os.path.exists(path):
            return f"❌ File not found: {path}"

        if not os.path.isfile(path):
            return f"❌ {path} is not a file"

        with open(path, "r", encoding="utf-8", errors="ignore") as f:
            line_count = sum(1 for _ in f)

        return f"📊 Line count: {line_count} lines in {path}"
    except Exception as e:
        return f"❌ Error counting lines: {e}"


@register_command("get file info {path}", safe=True)
def get_file_info(path: str):
    """Get comprehensive information about a file."""
    try:
        if not os.path.exists(path):
            return f"❌ File not found: {path}"

        stat_info = os.stat(path)

        # File type
        if os.path.isfile(path):
            file_type = "File"
        elif os.path.isdir(path):
            file_type = "Directory"
        else:
            file_type = "Special"

        # Size
        size = stat_info.st_size

        # Dates
        created = datetime.fromtimestamp(stat_info.st_ctime).strftime(
            "%Y-%m-%d %H:%M:%S"
        )
        modified = datetime.fromtimestamp(stat_info.st_mtime).strftime(
            "%Y-%m-%d %H:%M:%S"
        )

        # Extension
        _, extension = os.path.splitext(path)

        info = f"""📋 File Information for: {path}
Type: {file_type}
Size: {size} bytes
Extension: {extension or 'None'}
Created: {created}
Modified: {modified}"""

        return info
    except Exception as e:
        return f"❌ Error getting file info: {e}"


@register_command("get file hash {path}", safe=True)
def get_file_hash(path: str):
    """Get MD5 hash of a file."""
    try:
        if not os.path.exists(path):
            return f"❌ File not found: {path}"

        if not os.path.isfile(path):
            return f"❌ {path} is not a file"

        hash_md5 = hashlib.md5()
        with open(path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                hash_md5.update(chunk)

        file_hash = hash_md5.hexdigest()
        return f"🔒 MD5 hash: {file_hash}"
    except Exception as e:
        return f"❌ Error calculating hash: {e}"


@register_command("find files with extension {ext} in {directory}", safe=True)
def find_files_by_extension(ext: str, directory: str = "."):
    """Find all files with a specific extension in a directory."""
    try:
        if not os.path.exists(directory):
            return f"❌ Directory not found: {directory}"

        if not os.path.isdir(directory):
            return f"❌ {directory} is not a directory"

        # Ensure extension starts with dot
        if not ext.startswith("."):
            ext = "." + ext

        matching_files = []
        for root, dirs, files in os.walk(directory):
            for file in files:
                if file.lower().endswith(ext.lower()):
                    rel_path = os.path.relpath(os.path.join(root, file), directory)
                    matching_files.append(rel_path)

        if not matching_files:
            return f"🔍 No {ext} files found in {directory}"

        if len(matching_files) > 20:
            result = f"🔍 Found {len(matching_files)} {ext} files (showing first 20):\n"
            result += "\n".join(matching_files[:20])
            result += "\n..."
        else:
            result = f"🔍 Found {len(matching_files)} {ext} files:\n"
            result += "\n".join(matching_files)

        return result
    except Exception as e:
        return f"❌ Error searching for files: {e}"
