import logging
import os

from config import appname
from LCL.debug import Debug
from LCL.debug import debug
from LCL.emitter import Emitter

plugin_name = os.path.basename(os.path.dirname(__file__))
logger = logging.getLogger(f'{appname}.{plugin_name}')
Debug.setLogger(logger)

def plugin_start3(plugin_dir):
	debug(f'Startup with {plugin_dir=}')

	emitter = Emitter()
	emitter.start()
