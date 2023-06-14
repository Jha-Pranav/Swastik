
import logging
logger = logging.getLogger("diabetes")

class App:
    
    def __init__(self, settings):
        self.settings = settings    

    def start(self):
        logger.info("diabetes Starting")

    def stop(self):
        logger.info("diabetes Stopping")
