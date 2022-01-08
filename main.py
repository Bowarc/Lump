__Author__ = "Bowarc\nDiscord: Bowarc#4159"

import appfiles.app as app
import appfiles.utils.logger as logger
from appfiles.utils.constants import *

if __name__ == "__main__":
    l = logger.logger(level=0, logFile=ORIGINAL_PATH+LOGFILE,  # set it to constants.LOGFILE later
                      custom_exception_hook=True)
    Lump = app.Lump(l)
    Lump.run()
