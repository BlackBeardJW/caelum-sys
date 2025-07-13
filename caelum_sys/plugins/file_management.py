"""File management plugin for basic file and directory operations."""

from caelum_sys.registry import register_command
import os
import shutil


@register_command("create file at {path}")
def create_file(path: str):
    """Create a new empty file at the specified path."""
    try:
        with open(path, "w") as f:
            f.write("")
        return f"✅ Created file at: {path}"
    except Exception as e:
        return f"❌ Failed to create file at {path}: {e}"

@register_command("delete file at {path}")
def delete_file(path: str):
    """Delete a file at the specified path."""
    try:
        os.remove(path)
        return f"🗑️ Deleted file at: {path}"
    except FileNotFoundError:
        return f"❌ File not found: {path}"
    except PermissionError:
        return f"❌ Permission denied: Cannot delete {path}"
    except Exception as e:
        return f"❌ Failed to delete file at {path}: {e}"

@register_command("copy file {source} to {destination}")
def copy_file(source: str, destination: str):
    """Copy a file from source path to destination path."""
    try:
        shutil.copy(source, destination)
        return f"📄 Copied file from {source} to {destination}"
    except FileNotFoundError:
        return f"❌ Source file not found: {source}"
    except PermissionError:
        return f"❌ Permission denied: Cannot copy {source} to {destination}"
    except Exception as e:
        return f"❌ Copy failed: {e}"

@register_command("move file {source} to {destination}")
def move_file(source: str, destination: str):
    """Move (or rename) a file from source path to destination path."""
    try:
        shutil.move(source, destination)
        return f"📁 Moved file from {source} to {destination}"
    except FileNotFoundError:
        return f"❌ Source file not found: {source}"
    except PermissionError:
        return f"❌ Permission denied: Cannot move {source} to {destination}"
    except Exception as e:
        return f"❌ Move failed: {e}"

@register_command("list files in {directory}")
def list_files(directory: str):
    """List all files and directories in the specified directory."""
    try:
        files = os.listdir(directory)
        files.sort()
        if files:
            file_list = "\n".join(f"- {f}" for f in files)
            return f"📂 Files in {directory}:\n{file_list}"
        else:
            return f"📂 Directory {directory} is empty"
    except FileNotFoundError:
        return f"❌ Directory not found: {directory}"
    except PermissionError:
        return f"❌ Permission denied: Cannot access {directory}"
    except NotADirectoryError:
        return f"❌ Not a directory: {directory}"
    except Exception as e:
        return f"❌ Could not list files in {directory}: {e}"

@register_command("create directory at {path}")
def create_directory(path: str):
    """Create a new directory at the specified path."""
    try:
        os.makedirs(path, exist_ok=True)
        return f"📁 Created directory at: {path}"
    except PermissionError:
        return f"❌ Permission denied: Cannot create directory at {path}"
    except Exception as e:
        return f"❌ Failed to create directory at {path}: {e}"

# Additional utility functions for file operations (not registered as commands)

def _get_file_info(path: str):
    """Get detailed information about a file or directory."""
    try:
        stat_info = os.stat(path)
        return {
            'size': stat_info.st_size,
            'is_file': os.path.isfile(path),
            'is_directory': os.path.isdir(path),
            'permissions': oct(stat_info.st_mode)[-3:],
            'modified': stat_info.st_mtime
        }
    except:
        return None

def _safe_path_join(*args):
    """Safely join path components to prevent directory traversal attacks."""
    return os.path.normpath(os.path.join(*args))
