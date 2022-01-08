import sys
import os

# KEEP PATH WITH \\ BESIDE USING /

ORIGINAL_PATH = os.path.abspath(os.path.dirname(sys.argv[0])) + "\\"

LOGFILE = "Lump.log"

# plugins
PLUGINS_PATH = "appfiles\\plugins\\"
PLUGIN_ABSOLUTE_PATH = f"{ORIGINAL_PATH}{PLUGINS_PATH}"
DEFAULT_PLUGIN_FILE_NAME = "defaultPlugin.py"
SKIPPED_PLUGIN_NAMES = ["__init__.py", DEFAULT_PLUGIN_FILE_NAME]
PLUGIN_CLASS_NAME = "plugin"
PLUGIN_SORTING_ORDER = ["defaultPlugin.py", "testPlugin.py",
                        "plugin2.py"]  # and the rest is untouched
