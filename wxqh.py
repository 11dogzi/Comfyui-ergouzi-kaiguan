def is_context_empty(ctx):
    return not ctx or all(v is None for v in ctx.values())

def get_category(sub_dirs=None):
    return "Switch" if sub_dirs is None else "{}/utils".format("Switch")

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

class EGRYDZQHNode:

    NAME = get_name("Any Switch")
    CATEGORY = get_category()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {f"input{i}": (any_type,) for i in range(1, 3)},
        }

    RETURN_TYPES = (any_type,)
    RETURN_NAMES = ('output',)
    FUNCTION = "switch"
    CATEGORY = "2🐕kaiguan"

    def switch(self, **inputs):
        for input_name, value in inputs.items():
            if not is_none(value):
                return (value,)
        return (None,)

NODE_CLASS_MAPPINGS = {
    "EGRYDZQHNode": EGRYDZQHNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EGRYDZQHNode": "Recursive switching🔀"
}

