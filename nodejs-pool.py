#!/usr/bin/env python

from nodes import PoolController
from nodes import PoolNode
from nodes import SwitchNode
import udi_interface
import sys

LOGGER = udi_interface.LOGGER
LOG_HANDLER = udi_interface.LOG_HANDLER

""" Grab My Controller Node (optional) """
if __name__ == "__main__":
    try:
        LOGGER.debug("Staring Jaguar Interface")
        polyglot = udi_interface.Interface(
            [PoolController, SwitchNode, PoolNode])
        polyglot.start()
        control = PoolController(
            polyglot, 'controller', 'controller', 'Pool Controller Nixie')
        polyglot.runForever()
    except (KeyboardInterrupt, SystemExit):
        polyglot.stop()
        sys.exit(0)
    except Exception as err:
        LOGGER.error('Exception: {0}'.format(err), exc_info=True)
        sys.exit(0)
