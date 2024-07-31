class GroupSwitchNode:
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

    RETURN_TYPES = ("*",)
    FUNCTION = "process"

    CATEGORY = "2🐕kaiguan"

    def process(self, smooth_edge_switch):
        return (smooth_edge_switch,)

NODE_CLASS_MAPPINGS = {
    "GroupSwitchNode": GroupSwitchNode
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "GroupSwitchNode": "All Ignore👁️‍🗨️"
}
