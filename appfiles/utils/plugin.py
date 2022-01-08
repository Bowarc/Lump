import os
from appfiles.utils.constants import *
import importlib
import imp


class handler():
    def __init__(self, logger):
        self.logger = logger

        self.plugins = []

        # maybe redo this and add a function to
        # load plugin from config file
        self.load_plugins()

        self.test_plugins()

    def load_plugins(self):
        self.logger.debug("Searching for plugins. . .")

        for item_name in os.listdir(PLUGINS_PATH):
            if os.path.isfile(os.path.join(PLUGINS_PATH, item_name)) and item_name != DEFAULT_PLUGIN_FILE_NAME:
                plugin_file = (os.path.join(
                    PLUGINS_PATH, item_name)).replace("/", "\\")
                self.logger.debug(f"Plugin found: {item_name}, loading. .")
                plugin_class = self.load(plugin_file)
                if plugin_class:
                    self.logger.info(f"Successfully loaded plugin: {item_name[:-3]}.\nStarting module: {item_name[:-3]}")
                    plugin_class = plugin_class(self.logger)
                    self.plugins.append(plugin_class)
                else:
                    self.logger.warning(f"Failled to load plugin: {item_name[:-3]}.")

    def load(self, filepath):
        class_inst = None
        expected_class = PLUGIN_CLASS_NAME

        mod_name, file_ext = os.path.splitext(os.path.split(filepath)[-1])

        if file_ext.lower() == '.py':
            py_mod = imp.load_source(mod_name, filepath)

        elif file_ext.lower() == '.pyc':
            py_mod = imp.load_compiled(mod_name, filepath)

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
