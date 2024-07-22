import json

def convert_value(value):
    try:
        # Try to convert the value to a Python object
        converted_value = json.loads(value)
        return converted_value
    except (json.JSONDecodeError, TypeError):
        # If conversion fails, return the original string
        return value
