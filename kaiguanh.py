import torch
import random
import json

class EGRWGL:
    @classmethod
    def INPUT_TYPES(cls):
        return {
            "hidden": {
                "运行次数": ("INT", {
                    "default": 1,
                    "min": 1,
                    "max": 1000
                }),
            }
        }

    RETURN_TYPES = ()
    RETURN_NAMES = ("剩余运行次数",)
    FUNCTION = "manage_tasks"
    CATEGORY = "2🐕kaiguan"
    
    def manage_tasks(self, 运行次数):
        return (运行次数,)
NODE_CLASS_MAPPINGS = {
    "EGRWGL": EGRWGL
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EGRWGL": "2🐕任务管理器"
}