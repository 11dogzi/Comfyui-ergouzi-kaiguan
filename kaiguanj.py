import random
from datetime import datetime
def category_type():
    return "utils"

def node_name(name):
    return f"ergouzi {name}"
initial_random_state = random.getstate()
random.seed(datetime.now().timestamp())
ergouziseed_random_state = random.getstate()
random.setstate(initial_random_state)


def generate_unique_seed():
    global ergouziseed_random_state
    prev_random_state = random.getstate()
    random.setstate(ergouziseed_random_state)
    seed = random.randint(1, 1125899906842624)
    ergouziseed_random_state = random.getstate()
    random.setstate(prev_random_state)
    return seed


class EGSEED:
    NAME = node_name('Seed')
    CATEGORY = category_type()

    @classmethod
    def INPUT_TYPES(cls):
        return {
            "required": {
                "seed": ("INT", {
                    "default": -1,
                    "min": -1125899906842624,
                    "max": 1125899906842624
                }),
            },
            "hidden": {
                "prompt": "PROMPT",
                "extra_pnginfo": "EXTRA_PNGINFO",
                "unique_id": "UNIQUE_ID",
            },
        }

    RETURN_TYPES = ("INT",)
    RETURN_NAMES = ("SEED",)
    FUNCTION = "main"
    CATEGORY = "2🐕kaiguan"

    @classmethod
    def IS_CHANGED(cls, seed, prompt=None, extra_pnginfo=None, unique_id=None):
        if seed in (-1, -2, -3):
            return generate_unique_seed()
        return seed

    def main(self, seed=0, prompt=None, extra_pnginfo=None, unique_id=None):
        try:
            original_seed = seed
            if seed in (-1, -2, -3):
                seed = generate_unique_seed()
            try:
                if unique_id is not None:
                    if extra_pnginfo is not None and 'workflow' in extra_pnginfo:
                        workflow_node = next(
                            (x for x in extra_pnginfo['workflow']['nodes'] if x['id'] == int(unique_id)), None)
                        if workflow_node is not None and 'widgets_values' in workflow_node:
                            for index, widget_value in enumerate(workflow_node['widgets_values']):
                                if widget_value in (-1, -2, -3) or widget_value == original_seed:
                                    workflow_node['widgets_values'][index] = seed
                    if prompt is not None and str(unique_id) in prompt:
                        prompt_node = prompt.get(str(unique_id))
                        if prompt_node is not None and 'inputs' in prompt_node and 'seed' in prompt_node['inputs']:
                            prompt_node['inputs']['seed'] = seed
            except Exception:
                pass
            
            return (seed,)
        except Exception:
            return (42,)
NODE_CLASS_MAPPINGS = {
    "EGSEED": EGSEED
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "EGSEED": "2🐕EGSEED"
}