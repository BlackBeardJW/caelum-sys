"""
Math and calculation plugin for numerical operations and unit conversions.
"""

from caelum_sys.registry import register_command
import math
import random
import re

@register_command("calculate", safe=True)
def calculate(expression: str):
    """Calculate a mathematical expression safely."""
    try:
        # Remove any potentially dangerous functions/keywords
        dangerous_keywords = ['import', 'exec', 'eval', 'open', 'file', '__']
        if any(keyword in expression.lower() for keyword in dangerous_keywords):
            return "❌ Expression contains unsafe operations"
        
        # Allow only basic math operations and functions
        allowed_names = {
            "abs": abs, "round": round, "min": min, "max": max,
            "sum": sum, "pow": pow, "sqrt": math.sqrt, "sin": math.sin,
            "cos": math.cos, "tan": math.tan, "log": math.log,
            "pi": math.pi, "e": math.e
        }
        
        # Use eval with restricted globals for safety
        result = eval(expression, {"__builtins__": {}}, allowed_names)
        return f"🧮 Result: {result}"
    except Exception as e:
        return f"❌ Calculation error: {e}"

@register_command("generate random number between {min_val} and {max_val}", safe=True)
def random_number(min_val: int, max_val: int):
    """Generate a random number between min and max values."""
    try:
        if min_val > max_val:
            min_val, max_val = max_val, min_val
        result = random.randint(min_val, max_val)
        return f"🎲 Random number: {result}"
    except Exception as e:
        return f"❌ Error generating random number: {e}"

@register_command("convert temperature {value} {from_unit} to {to_unit}", safe=True)
def convert_temperature(value: float, from_unit: str, to_unit: str):
    """Convert temperature between Celsius, Fahrenheit, and Kelvin."""
    try:
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        # Convert to Celsius first
        if from_unit in ['f', 'fahrenheit']:
            celsius = (value - 32) * 5/9
        elif from_unit in ['k', 'kelvin']:
            celsius = value - 273.15
        elif from_unit in ['c', 'celsius']:
            celsius = value
        else:
            return "❌ Invalid temperature unit. Use C, F, or K"
        
        # Convert from Celsius to target
        if to_unit in ['f', 'fahrenheit']:
            result = celsius * 9/5 + 32
            unit_symbol = "°F"
        elif to_unit in ['k', 'kelvin']:
            result = celsius + 273.15
            unit_symbol = "K"
        elif to_unit in ['c', 'celsius']:
            result = celsius
            unit_symbol = "°C"
        else:
            return "❌ Invalid target unit. Use C, F, or K"
        
        return f"🌡️ {value}° {from_unit.upper()} = {result:.2f} {unit_symbol}"
    except Exception as e:
        return f"❌ Conversion error: {e}"

@register_command("convert length {value} {from_unit} to {to_unit}", safe=True)
def convert_length(value: float, from_unit: str, to_unit: str):
    """Convert length between common units."""
    try:
        # Conversion factors to meters
        to_meters = {
            'mm': 0.001, 'cm': 0.01, 'm': 1, 'km': 1000,
            'in': 0.0254, 'ft': 0.3048, 'yd': 0.9144, 'mi': 1609.34
        }
        
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in to_meters or to_unit not in to_meters:
            return "❌ Unsupported unit. Use: mm, cm, m, km, in, ft, yd, mi"
        
        # Convert to meters, then to target unit
        meters = value * to_meters[from_unit]
        result = meters / to_meters[to_unit]
        
        return f"📏 {value} {from_unit} = {result:.4f} {to_unit}"
    except Exception as e:
        return f"❌ Conversion error: {e}"

@register_command("convert weight {value} {from_unit} to {to_unit}", safe=True)
def convert_weight(value: float, from_unit: str, to_unit: str):
    """Convert weight between common units."""
    try:
        # Conversion factors to grams
        to_grams = {
            'mg': 0.001, 'g': 1, 'kg': 1000,
            'oz': 28.3495, 'lb': 453.592, 'ton': 1000000
        }
        
        from_unit = from_unit.lower()
        to_unit = to_unit.lower()
        
        if from_unit not in to_grams or to_unit not in to_grams:
            return "❌ Unsupported unit. Use: mg, g, kg, oz, lb, ton"
        
        # Convert to grams, then to target unit
        grams = value * to_grams[from_unit]
        result = grams / to_grams[to_unit]
        
        return f"⚖️ {value} {from_unit} = {result:.4f} {to_unit}"
    except Exception as e:
        return f"❌ Conversion error: {e}"

@register_command("calculate percentage {part} of {whole}", safe=True)
def calculate_percentage(part: float, whole: float):
    """Calculate what percentage one number is of another."""
    try:
        if whole == 0:
            return "❌ Cannot calculate percentage of zero"
        percentage = (part / whole) * 100
        return f"📊 {part} is {percentage:.2f}% of {whole}"
    except Exception as e:
        return f"❌ Calculation error: {e}"

@register_command("calculate tip {bill} at {percentage} percent", safe=True)
def calculate_tip(bill: float, percentage: float):
    """Calculate tip amount and total bill."""
    try:
        tip_amount = bill * (percentage / 100)
        total = bill + tip_amount
        return f"💰 Bill: ${bill:.2f}, Tip ({percentage}%): ${tip_amount:.2f}, Total: ${total:.2f}"
    except Exception as e:
        return f"❌ Calculation error: {e}"
