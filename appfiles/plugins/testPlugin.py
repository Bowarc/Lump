import appfiles.plugins.defaultPlugin as defaultPlugin


class plugin(defaultPlugin.plugin):
    def __init__(self, logger):
        super().__init__(logger)

        self.logger.debug("Working")

    def ping(self):
        return "im up (but from the child plugin)"
