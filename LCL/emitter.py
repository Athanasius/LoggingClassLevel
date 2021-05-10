import threading

from LCL.debug import Debug
from LCL.debug import debug

class Emitter(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)


    @classmethod
    def setRoute(cls):
        debug('debug from Emitter.setRoute')

    def run(self):
        self.setRoute()
