"""
Quick notes plugin for saving, retrieving, and managing text notes.
"""

from caelum_sys.registry import register_command
import json
import os
from datetime import datetime

# Notes file path
NOTES_FILE = "caelum_notes.json"

def _load_notes():
    """Load notes from file."""
    if os.path.exists(NOTES_FILE):
        try:
            with open(NOTES_FILE, 'r', encoding='utf-8') as f:
                return json.load(f)
        except:
            return {}
    return {}

def _save_notes(notes):
    """Save notes to file."""
    try:
        with open(NOTES_FILE, 'w', encoding='utf-8') as f:
            json.dump(notes, f, indent=2, ensure_ascii=False)
        return True
    except:
        return False

@register_command("save note {text}", safe=True)
def save_note(text: str):
    """Save a new note with automatic ID and timestamp."""
    try:
        notes = _load_notes()
        
        # Generate new ID
        note_id = str(len(notes) + 1)
        while note_id in notes:
            note_id = str(int(note_id) + 1)
        
        # Create note with timestamp
        note = {
            "text": text,
            "created": datetime.now().isoformat(),
            "id": note_id
        }
        
        notes[note_id] = note
        
        if _save_notes(notes):
            return f"📝 Note saved with ID: {note_id}"
        else:
            return "❌ Failed to save note to file"
    except Exception as e:
        return f"❌ Error saving note: {e}"

@register_command("list all notes", safe=True)
def list_notes():
    """List all saved notes with their IDs."""
    try:
        notes = _load_notes()
        
        if not notes:
            return "📝 No notes found"
        
        note_list = []
        for note_id, note in notes.items():
            created = datetime.fromisoformat(note["created"]).strftime("%Y-%m-%d %H:%M")
            preview = note["text"][:50] + "..." if len(note["text"]) > 50 else note["text"]
            note_list.append(f"ID {note_id} ({created}): {preview}")
        
        return f"📝 Found {len(notes)} notes:\n" + "\n".join(note_list)
    except Exception as e:
        return f"❌ Error listing notes: {e}"

@register_command("get note {note_id}", safe=True)
def get_note(note_id: str):
    """Retrieve a specific note by ID."""
    try:
        notes = _load_notes()
        
        if note_id not in notes:
            return f"❌ Note with ID '{note_id}' not found"
        
        note = notes[note_id]
        created = datetime.fromisoformat(note["created"]).strftime("%Y-%m-%d %H:%M:%S")
        
        return f"📝 Note ID {note_id} (created {created}):\n{note['text']}"
    except Exception as e:
        return f"❌ Error retrieving note: {e}"

@register_command("search notes for {keyword}", safe=True)
def search_notes(keyword: str):
    """Search notes for a specific keyword."""
    try:
        notes = _load_notes()
        keyword_lower = keyword.lower()
        
        matches = []
        for note_id, note in notes.items():
            if keyword_lower in note["text"].lower():
                preview = note["text"][:50] + "..." if len(note["text"]) > 50 else note["text"]
                matches.append(f"ID {note_id}: {preview}")
        
        if not matches:
            return f"🔍 No notes found containing '{keyword}'"
        
        return f"🔍 Found {len(matches)} notes containing '{keyword}':\n" + "\n".join(matches)
    except Exception as e:
        return f"❌ Error searching notes: {e}"

@register_command("delete note {note_id}", safe=False)
def delete_note(note_id: str):
    """Delete a note by ID."""
    try:
        notes = _load_notes()
        
        if note_id not in notes:
            return f"❌ Note with ID '{note_id}' not found"
        
        deleted_note = notes[note_id]
        del notes[note_id]
        
        if _save_notes(notes):
            preview = deleted_note["text"][:30] + "..." if len(deleted_note["text"]) > 30 else deleted_note["text"]
            return f"🗑️ Deleted note ID {note_id}: {preview}"
        else:
            return "❌ Failed to save changes"
    except Exception as e:
        return f"❌ Error deleting note: {e}"

@register_command("update note {note_id} with {new_text}", safe=False)
def update_note(note_id: str, new_text: str):
    """Update an existing note with new text."""
    try:
        notes = _load_notes()
        
        if note_id not in notes:
            return f"❌ Note with ID '{note_id}' not found"
        
        notes[note_id]["text"] = new_text
        notes[note_id]["modified"] = datetime.now().isoformat()
        
        if _save_notes(notes):
            return f"✏️ Updated note ID {note_id}"
        else:
            return "❌ Failed to save changes"
    except Exception as e:
        return f"❌ Error updating note: {e}"

@register_command("count notes", safe=True)
def count_notes():
    """Get the total number of saved notes."""
    try:
        notes = _load_notes()
        count = len(notes)
        return f"📊 Total notes: {count}"
    except Exception as e:
        return f"❌ Error counting notes: {e}"
