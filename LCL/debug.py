class Debug:

    @classmethod
    def setLogger(cls, logger):
        Debug.logger = logger

def debug(value):
    Debug.logger.debug(value)


def error(value):
    Debug.logger.error(value)
