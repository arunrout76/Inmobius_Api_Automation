import json

def convert_value(value):
    try:
        # Try to convert the value to a Python object
        converted_value = json.loads(value)
        return converted_value
    except (json.JSONDecodeError, TypeError):
        # If conversion fails, return the original string
        return value





# def convert_value(key, value):
#     try:
#         if key.startswith('primary_contact_info'):
#             # If the key suggests it's part of the nested object, parse it accordingly
#             return json.loads(value)
#         # Convert to Python object
#         return json.loads(value)
#     except (json.JSONDecodeError, TypeError):
#         # If conversion fails, return the original string
#         return value
