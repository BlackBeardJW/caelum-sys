import os
from caelum_sys.registry import register_command

@register_command("list files in")
def list_files(command: str):
    path = command[len("list files in"):].strip() or "."
    try:
        files = os.listdir(path)
        return f"📁 Files in '{path}':\n" + "\n".join(files)
    except Exception as e:
        return f"❌ Error listing files: {e}"

@register_command("delete file")
def delete_file(command: str):
    filename = command[len("delete file"):].strip()
    try:
        os.remove(filename)
        return f"🗑️ Deleted '{filename}'"
    except Exception as e:
        return f"❌ Failed to delete '{filename}': {e}"

@register_command("create file")
def create_file(command: str):
    filename = command[len("create file"):].strip()
    try:
        with open(filename, "w") as f:
            f.write("")
        return f"📄 Created empty file '{filename}'"
    except Exception as e:
        return f"❌ Failed to create file '{filename}': {e}"
