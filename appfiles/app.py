from PyQt5.QtWidgets import QApplication

import appfiles.utils.plugin as plugin

import appfiles.uis.mainUi as mainUi


class Lump():
    def __init__(self, logger):
        self.logger = logger
        self.plugins_handler = plugin.handler(logger)

        self.qApp = QApplication([])
        self.window = mainUi.window(self.logger, self.plugins_handler.plugins)

    def run(self):
        self.logger.debug("Start running. . .")

        self.window.show()

        self.qApp.exec()
        self.logger.debug("Stopping. . .")
