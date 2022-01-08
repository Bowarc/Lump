import os
from appfiles.utils.constants import *
# import importlib
import imp


class handler():
    def __init__(self, logger):
        self.logger = logger

        self.plugins = self.load_plugins()

        # maybe redo this and add a function to
        # load plugin from config file

        self.test_plugins()

    def load_plugins(self):
        self.logger.debug("Searching for plugins...")
        plugin_files_paths = []
        for item_name in os.listdir(PLUGIN_ABSOLUTE_PATH):
            if os.path.isfile(os.path.join(PLUGIN_ABSOLUTE_PATH, item_name)) and item_name not in SKIPPED_PLUGIN_NAMES:
                plugin_file = item_name
                plugin_files_paths.append(plugin_file)

        if len(plugin_files_paths) == 0:
            self.logger.debug("Found 0 module.")
            return []
        elif len(plugin_files_paths) == 1:
            self.logger.debug(f"Found: 1 module\nLoading. .")
        else:
            self.logger.debug(f"Found: {len(plugin_files_paths)} modules\nLoading. .")
        plugins_classes = []
        for plugin_file in self.custom_sorting(plugin_files_paths, PLUGIN_SORTING_ORDER):
            self.logger.info(f"Loading {plugin_file}")
            plugin_class = self.load(plugin_file)
            if plugin_class:
                self.logger.info(f"Successfully loaded plugin: {plugin_file[:-3]}")
                # Booting up the plugin's class
                plugin_class = plugin_class(self.logger)
                plugins_classes.append(plugin_class)
            else:
                self.logger.warning(f"Failled to load plugin: {plugin_file[:-3]}")
        return plugins_classes

    def load(self, fileName):
        class_inst = None
        expected_class = PLUGIN_CLASS_NAME

        filepath = PLUGIN_ABSOLUTE_PATH + fileName

        name, ext = os.path.splitext(os.path.split(filepath)[-1])

        if ext.lower() == '.py':
            py_mod = imp.load_source(name, filepath)

        elif ext.lower() == '.pyc':
            py_mod = imp.load_compiled(name, filepath)

        if hasattr(py_mod, expected_class):
            # Class could be started here with:
            # class_inst = getattr(py_mod, expected_class)(self.logger)
            # but i think it's better to start it later and just get the object for
            class_inst = getattr(py_mod, expected_class)

        return class_inst

    def test_plugins(self):
        self.logger.debug(
            "Pinging plugins to see if they are corectly loaded.")
        for plugin in self.plugins:
            self.logger.debug(f"{str(plugin)}: {plugin.ping()}")

    def custom_sorting(self, modules, order):
        output = []
        for o in order:
            if o in modules:
                # self.logger.info(f"Sort found: {o}")
                output.append(modules.pop(modules.index(o)))
            else:
                pass
                # self.logger.warning(f"Found no match for: {o}")

        output.extend(modules)
        return output
