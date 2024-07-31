def is_context_empty(ctx):
    return not ctx or all(v is None for v in ctx.values())

def get_name(name):
    return '{}'.format(name)

class AnyType(str):
    def __ne__(self, __value: object) -> bool:
        return False

any_type = AnyType("*")

def is_none(value):
    if value is not None:
        if isinstance(value, dict) and 'model' in value and 'clip' in value:
            return is_context_empty(value)
    return value is None

def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        return None

def convert_to_float(value):
    try:
        return float(value)
    except ValueError:
        return None

def convert_to_str(value):
    return str(value)

class hulue:

    def __init__(self):
        pass
    
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {"*": (any_type,)},
            "optional": {},
        }

    RETURN_TYPES = ()
    FUNCTION = "execute"

    CATEGORY = "2🐕kaiguan"

    def execute(self, any_type):
        if any_type:
            print("Switch is ON")
        else:
            print("Switch is OFF")

NODE_CLASS_MAPPINGS = {
    "hulue": hulue
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "hulue": "hulue🔃"
}
