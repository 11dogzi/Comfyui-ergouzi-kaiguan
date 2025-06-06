class GroupSwitchNodi:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "process"

    CATEGORY = "2🐕kaiguan"
NODE_CLASS_MAPPINGS = {
    "GroupSwitchNodi": GroupSwitchNodi
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GroupSwitchNodi": "2🐕Group"
}