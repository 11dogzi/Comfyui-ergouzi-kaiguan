import os
import sys
import importlib
import shutil
import filecmp
python = sys.executable
extensions_folder = os.path.join(os.path.dirname(os.path.realpath(sys.argv[0])),
                                 "web", "extensions", "EG_KG")
javascript_folder = os.path.join(os.path.dirname(os.path.dirname(os.path.realpath(__file__))), "Comfyui-ergouzi-kaiguan", "web")
if not os.path.exists(extensions_folder):
    print('Creating the "web/extensions/EG_KG" folder')
    os.makedirs(extensions_folder)
result = filecmp.dircmp(javascript_folder, extensions_folder)
if result.left_only or result.diff_files:
    print('Update to JavaScript files detected')
    file_list = list(result.left_only)
    file_list.extend(x for x in result.diff_files if x not in file_list)

    for file in file_list:
        print(f'Copying {file} to extensions folder')
        src_file = os.path.join(javascript_folder, file)
        dst_file = os.path.join(extensions_folder, file)
        if os.path.exists(dst_file):
            os.remove(dst_file)
        shutil.copy(src_file, dst_file)
NODE_CLASS_MAPPINGS = {}
NODE_DISPLAY_NAME_MAPPINGS = {}
def load_nodes():
    current_dir = os.path.dirname(__file__)
    for filename in os.listdir(current_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            module_name = filename[:-3]
            try:
                module = importlib.import_module(f".{module_name}", package=__name__)
                if hasattr(module, "NODE_CLASS_MAPPINGS"):
                    NODE_CLASS_MAPPINGS.update(module.NODE_CLASS_MAPPINGS)
                if hasattr(module, "NODE_DISPLAY_NAME_MAPPINGS"):
                    NODE_DISPLAY_NAME_MAPPINGS.update(module.NODE_DISPLAY_NAME_MAPPINGS)
            except Exception as e:
                print(f"Error loading module {module_name}: {e}")
load_nodes()

__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS"]
