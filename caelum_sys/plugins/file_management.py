from caelum_sys.registry import register_command
import os
import shutil

@register_command("create file at {path}")
def create_file(path: str):
    try:
        with open(path, "w") as f:
            f.write("")
        return f"✅ Created file at: {path}"
    except Exception as e:
        return f"❌ Failed to create file at {path}: {e}"

@register_command("delete file at {path}")
def delete_file(path: str):
    try:
        os.remove(path)
        return f"🗑️ Deleted file at: {path}"
    except Exception as e:
        return f"❌ Failed to delete file at {path}: {e}"

@register_command("copy file {source} to {destination}")
def copy_file(source: str, destination: str):
    try:
        shutil.copy(source, destination)
        return f"📄 Copied file from {source} to {destination}"
    except Exception as e:
        return f"❌ Copy failed: {e}"

@register_command("move file {source} to {destination}")
def move_file(source: str, destination: str):
    try:
        shutil.move(source, destination)
        return f"📁 Moved file from {source} to {destination}"
    except Exception as e:
        return f"❌ Move failed: {e}"

@register_command("list files in {directory}")
def list_files(directory: str):
    try:
        files = os.listdir(directory)
        return f"📂 Files in {directory}:\n" + "\n".join(f"- {f}" for f in files)
    except Exception as e:
        return f"❌ Could not list files in {directory}: {e}"

@register_command("create directory at {path}")
def create_directory(path: str):
    try:
        os.makedirs(path, exist_ok=True)
        return f"📁 Created directory at: {path}"
    except Exception as e:
        return f"❌ Failed to create directory at {path}: {e}"
