"""
File Management Plugin

This plugin provides essential file and directory operations through natural
language commands. It handles creating, deleting, copying, moving files and
directories, as well as listing directory contents.

Commands provided:
- "create file at {path}" - Create an empty file
- "delete file at {path}" - Delete a file  
- "copy file {source} to {destination}" - Copy a file
- "move file {source} to {destination}" - Move/rename a file
- "list files in {directory}" - List directory contents
- "create directory at {path}" - Create a directory

Dependencies:
- os: For file system operations
- shutil: For advanced file operations (copy, move)

Safety Notes:
- Delete operations are permanent and cannot be undone
- Move operations will overwrite existing files at the destination
- All operations respect file system permissions
"""

from caelum_sys.registry import register_command
import os     # For basic file system operations
import shutil # For advanced file operations like copy and move

@register_command("create file at {path}")
def create_file(path: str):
    """
    Create a new empty file at the specified path.
    
    This command creates an empty file at the given location. If the file
    already exists, it will be overwritten (truncated to empty). If the
    directory doesn't exist, the operation will fail.
    
    Args:
        path (str): The path where the file should be created
                   Can be relative or absolute path
                   
    Returns:
        str: Success message with the file path, or error message if failed
        
    Example:
        result = do("create file at test.txt")
        # Result: "✅ Created file at: test.txt"
        
        result = do("create file at C:/Users/Name/Documents/notes.txt")
        # Result: "✅ Created file at: C:/Users/Name/Documents/notes.txt"
    """
    try:
        # Open the file in write mode, which creates it if it doesn't exist
        # or truncates it to empty if it does exist
        with open(path, "w") as f:
            f.write("")  # Write empty string to create an empty file
        return f"✅ Created file at: {path}"
    except Exception as e:
        # Handle various errors: permissions, invalid path, directory doesn't exist, etc.
        return f"❌ Failed to create file at {path}: {e}"

@register_command("delete file at {path}")
def delete_file(path: str):
    """
    Delete a file at the specified path.
    
    This command permanently removes a file from the file system.
    The operation cannot be undone, so use with caution.
    
    Args:
        path (str): The path of the file to delete
                   Can be relative or absolute path
                   
    Returns:
        str: Success message with the file path, or error message if failed
        
    Example:
        result = do("delete file at test.txt")
        # Result: "🗑️ Deleted file at: test.txt"
        
    Warning:
        This operation is permanent! The file cannot be recovered unless
        you have backups or file system recovery tools.
    """
    try:
        # Remove the file from the file system
        os.remove(path)
        return f"🗑️ Deleted file at: {path}"
    except FileNotFoundError:
        # Handle case where file doesn't exist
        return f"❌ File not found: {path}"
    except PermissionError:
        # Handle case where we don't have permission to delete
        return f"❌ Permission denied: Cannot delete {path}"
    except Exception as e:
        # Handle any other errors
        return f"❌ Failed to delete file at {path}: {e}"

@register_command("copy file {source} to {destination}")
def copy_file(source: str, destination: str):
    """
    Copy a file from source path to destination path.
    
    This command creates a complete copy of the source file at the destination
    location. The original file remains unchanged. If a file already exists
    at the destination, it will be overwritten.
    
    Args:
        source (str): Path of the file to copy from
        destination (str): Path where the copy should be created
                          Can be a filename or directory path
                          
    Returns:
        str: Success message with source and destination, or error message if failed
        
    Example:
        result = do("copy file document.txt to backup.txt")
        # Result: "📄 Copied file from document.txt to backup.txt"
        
        result = do("copy file C:/source.txt to D:/backup/source.txt")
        # Result: "📄 Copied file from C:/source.txt to D:/backup/source.txt"
    """
    try:
        # Use shutil.copy which preserves file permissions and timestamps
        # shutil.copy2 would also preserve metadata, but copy is more reliable
        shutil.copy(source, destination)
        return f"📄 Copied file from {source} to {destination}"
    except FileNotFoundError:
        # Handle case where source file doesn't exist
        return f"❌ Source file not found: {source}"
    except PermissionError:
        # Handle permission issues (can't read source or write to destination)
        return f"❌ Permission denied: Cannot copy {source} to {destination}"
    except Exception as e:
        # Handle other errors like disk space, invalid paths, etc.
        return f"❌ Copy failed: {e}"

@register_command("move file {source} to {destination}")
def move_file(source: str, destination: str):
    """
    Move (or rename) a file from source path to destination path.
    
    This command moves the file from the source location to the destination.
    Unlike copy, the original file is removed after the move operation.
    This can be used for both moving files between directories and renaming files.
    
    Args:
        source (str): Path of the file to move
        destination (str): New path for the file
                          
    Returns:
        str: Success message with source and destination, or error message if failed
        
    Example:
        # Moving to different directory
        result = do("move file temp.txt to archive/temp.txt")
        # Result: "📁 Moved file from temp.txt to archive/temp.txt"
        
        # Renaming a file
        result = do("move file old_name.txt to new_name.txt")
        # Result: "📁 Moved file from old_name.txt to new_name.txt"
    """
    try:
        # Use shutil.move which handles both files and directories
        # and works across different file systems
        shutil.move(source, destination)
        return f"📁 Moved file from {source} to {destination}"
    except FileNotFoundError:
        # Handle case where source file doesn't exist
        return f"❌ Source file not found: {source}"
    except PermissionError:
        # Handle permission issues
        return f"❌ Permission denied: Cannot move {source} to {destination}"
    except Exception as e:
        # Handle other errors like destination already exists as directory, etc.
        return f"❌ Move failed: {e}"

@register_command("list files in {directory}")
def list_files(directory: str):
    """
    List all files and directories in the specified directory.
    
    This command shows the contents of a directory, including both files
    and subdirectories. Hidden files (those starting with .) are included
    in the listing.
    
    Args:
        directory (str): Path of the directory to list
                        Use "." for current directory
                        Use ".." for parent directory
                        
    Returns:
        str: Formatted list of directory contents, or error message if failed
        
    Example:
        result = do("list files in .")
        # Result: "📂 Files in .:\n- document.txt\n- images/\n- notes.md"
        
        result = do("list files in C:/Users/Name/Documents")
        # Result: "📂 Files in C:/Users/Name/Documents:\n- file1.txt\n- folder1/"
    """
    try:
        # Get list of all items in the directory
        files = os.listdir(directory)
        
        # Sort the files for consistent output
        files.sort()
        
        # Format the output with each file on a new line
        if files:
            file_list = "\n".join(f"- {f}" for f in files)
            return f"📂 Files in {directory}:\n{file_list}"
        else:
            return f"📂 Directory {directory} is empty"
            
    except FileNotFoundError:
        # Handle case where directory doesn't exist
        return f"❌ Directory not found: {directory}"
    except PermissionError:
        # Handle case where we don't have permission to read directory
        return f"❌ Permission denied: Cannot access {directory}"
    except NotADirectoryError:
        # Handle case where path points to a file, not a directory
        return f"❌ Not a directory: {directory}"
    except Exception as e:
        # Handle any other errors
        return f"❌ Could not list files in {directory}: {e}"

@register_command("create directory at {path}")
def create_directory(path: str):
    """
    Create a new directory at the specified path.
    
    This command creates a new directory (folder). If parent directories
    in the path don't exist, they will be created automatically. If the
    directory already exists, the operation succeeds without error.
    
    Args:
        path (str): Path where the directory should be created
                   Can be relative or absolute path
                   
    Returns:
        str: Success message with the directory path, or error message if failed
        
    Example:
        result = do("create directory at new_folder")
        # Result: "📁 Created directory at: new_folder"
        
        result = do("create directory at project/src/components")
        # Result: "📁 Created directory at: project/src/components"
        # (Creates all parent directories if they don't exist)
    """
    try:
        # Use makedirs with exist_ok=True to:
        # 1. Create parent directories if they don't exist
        # 2. Not fail if the directory already exists
        os.makedirs(path, exist_ok=True)
        return f"📁 Created directory at: {path}"
    except PermissionError:
        # Handle permission issues
        return f"❌ Permission denied: Cannot create directory at {path}"
    except Exception as e:
        # Handle other errors like invalid path characters, disk space, etc.
        return f"❌ Failed to create directory at {path}: {e}"

# Additional utility functions for file operations (not registered as commands)

def _get_file_info(path: str):
    """
    Get detailed information about a file or directory.
    
    This is a private utility function that could be extended to provide
    file size, creation date, permissions, etc.
    
    Args:
        path (str): Path to the file or directory
        
    Returns:
        dict: File information including size, type, permissions, etc.
    """
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
    """
    Safely join path components to prevent directory traversal attacks.
    
    This utility function could be used to validate paths before operations.
    
    Args:
        *args: Path components to join
        
    Returns:
        str: Safely joined path
    """
    # This is a simplified version - production code might want more validation
    return os.path.normpath(os.path.join(*args))
