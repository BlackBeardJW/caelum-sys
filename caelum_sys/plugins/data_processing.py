"""
Data processing and conversion plugin for encoding, hashing, and format transformations.
"""

from caelum_sys.registry import register_command
import json
import csv
import base64
import hashlib
import uuid
from io import StringIO

@register_command("convert json to csv", safe=True)
def json_to_csv(json_data: str):
    """Convert JSON data to CSV format."""
    try:
        data = json.loads(json_data)
        
        # Handle list of dictionaries
        if isinstance(data, list) and data and isinstance(data[0], dict):
            output = StringIO()
            writer = csv.DictWriter(output, fieldnames=data[0].keys())
            writer.writeheader()
            writer.writerows(data)
            return f"📊 CSV conversion successful:\n{output.getvalue()}"
        else:
            return "❌ JSON must be a list of objects for CSV conversion"
    except json.JSONDecodeError:
        return "❌ Invalid JSON format"
    except Exception as e:
        return f"❌ Conversion failed: {e}"

@register_command("encode base64", safe=True)
def encode_base64(text: str):
    """Encode text to base64."""
    try:
        encoded = base64.b64encode(text.encode('utf-8')).decode('utf-8')
        return f"🔐 Base64 encoded: {encoded}"
    except Exception as e:
        return f"❌ Encoding failed: {e}"

@register_command("decode base64", safe=True)
def decode_base64(encoded: str):
    """Decode base64 text."""
    try:
        decoded = base64.b64decode(encoded).decode('utf-8')
        return f"🔓 Base64 decoded: {decoded}"
    except Exception as e:
        return f"❌ Decoding failed: {e}"

@register_command("generate uuid", safe=True)
def generate_uuid():
    """Generate a random UUID."""
    new_uuid = str(uuid.uuid4())
    return f"🆔 Generated UUID: {new_uuid}"

@register_command("hash text with md5", safe=True)
def hash_md5(text: str):
    """Generate MD5 hash of text."""
    hash_result = hashlib.md5(text.encode('utf-8')).hexdigest()
    return f"🔒 MD5 hash: {hash_result}"

@register_command("hash text with sha256", safe=True)
def hash_sha256(text: str):
    """Generate SHA256 hash of text."""
    hash_result = hashlib.sha256(text.encode('utf-8')).hexdigest()
    return f"🔒 SHA256 hash: {hash_result}"

@register_command("validate json", safe=True)
def validate_json(json_string: str):
    """Validate if a string is valid JSON."""
    try:
        json.loads(json_string)
        return "✅ Valid JSON format"
    except json.JSONDecodeError as e:
        return f"❌ Invalid JSON: {e}"

@register_command("format json", safe=True)
def format_json(json_string: str):
    """Pretty format JSON string."""
    try:
        data = json.loads(json_string)
        formatted = json.dumps(data, indent=2, ensure_ascii=False)
        return f"📋 Formatted JSON:\n{formatted}"
    except json.JSONDecodeError as e:
        return f"❌ Invalid JSON: {e}"

@register_command("extract json keys", safe=True)
def extract_json_keys(json_string: str):
    """Extract all keys from a JSON object."""
    try:
        data = json.loads(json_string)
        if isinstance(data, dict):
            keys = list(data.keys())
            return f"🔑 JSON keys: {', '.join(keys)}"
        else:
            return "❌ JSON must be an object to extract keys"
    except json.JSONDecodeError as e:
        return f"❌ Invalid JSON: {e}"

@register_command("url encode text", safe=True)
def url_encode(text: str):
    """URL encode text."""
    from urllib.parse import quote_plus
    encoded = quote_plus(text)
    return f"🔗 URL encoded: {encoded}"

@register_command("url decode text", safe=True)
def url_decode(encoded_text: str):
    """URL decode text."""
    from urllib.parse import unquote_plus
    try:
        decoded = unquote_plus(encoded_text)
        return f"🔗 URL decoded: {decoded}"
    except Exception as e:
        return f"❌ Decoding failed: {e}"
