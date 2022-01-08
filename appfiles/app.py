import appfiles.utils.plugin as plugin


class Lump():
    def __init__(self, logger):
        self.logger = logger

        self.pluggins_handler = plugin.handler(logger)

    def run(self):
        self.logger.debug("Start running. . .")
