import sys
import os
# KEEP PATH WITH \\ BESIDE USING /

# All
ORIGINAL_PATH = os.path.abspath(os.path.dirname(sys.argv[0])) + "\\"

APPLICATION_TITLE = "Lump"

# Logging
LOGFILE = "Lump.log"

# Plugins
PLUGINS_PATH = "appfiles\\plugins\\"
PLUGIN_ABSOLUTE_PATH = f"{ORIGINAL_PATH}{PLUGINS_PATH}"
DEFAULT_PLUGIN_FILE_NAME = "defaultPlugin.py"
SKIPPED_PLUGIN_NAMES = ["__init__.py", DEFAULT_PLUGIN_FILE_NAME]
PLUGIN_CLASS_NAME = "plugin"
PLUGIN_SORTING_ORDER = ["defaultPlugin.py", "testPlugin.py",
                        "plugin2.py"]  # and the rest is untouched

# Window
WINDOW_SIZE = (800, 600)
WINDOW_TITLE = "Lump window"

# Qss
QSS_PATH = "appfiles\\src\\qss\\"

# Images
QSS_PATH = "appfiles\\src\\images\\"

# Sounds
QSS_PATH = "appfiles\\src\\sounds\\"

# Fonts
QSS_PATH = "appfiles\\src\\fonts\\"
