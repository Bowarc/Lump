
class plugin:
    def __init__(self, logger):
        self.logger = logger
        self.logger.debug("Default plugin init")

    def ping(self):
        return "I'm up"
