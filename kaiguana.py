class GroupSwitchNodeeee:
    def __init__(self):
        pass

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "smooth_edge_switch": ("BOOLEAN", {
                    "default": True,
                    "display": "hidden"
                }),
            }
        }

    RETURN_TYPES = ()
    FUNCTION = "process"

    CATEGORY = "2🐕kaiguan"

NODE_CLASS_MAPPINGS = {
    "GroupSwitchNodeeee": GroupSwitchNodeeee
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GroupSwitchNodeeee": "Universal switch▶️"
}