# https://stackoverflow.com/questions/11927278/how-to-configure-logging-in-python

import os
import logging 
from datetime import datetime

class Logger(object):
    mlogger = None
    def __init__(self, name, filename="_"):
        logging.basicConfig()
        logging.getLogger().handlers.clear()
        logger = logging.getLogger(name)
        logger.setLevel(logging.INFO)
        
        if self.mlogger is None:
            # Create handlers
            fileLogPath = './logs/{:%Y-%m-%d}-apiservice'.format(datetime.now())
            fileLogPath = fileLogPath + "_" + filename+'.log'
            c_handler = logging.StreamHandler()
            f_handler = logging.FileHandler(fileLogPath)
            
            c_handler.setLevel(logging.INFO)
            f_handler.setLevel(logging.ERROR)
            
            # Create formatters and add it to handlers
            # c_format = logging.Formatter('%(filename)s:%(lineno)s_%(name)s - %(levelname)s - %(message)s')
            c_format = logging.Formatter('%(filename)s:%(lineno)s_%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            f_format = logging.Formatter('%(filename)s:%(lineno)s_%(asctime)s - %(name)s - %(levelname)s - %(message)s')
            c_handler.setFormatter(c_format)
            f_handler.setFormatter(f_format)
            
            # Add handlers to the logger
            if logger.hasHandlers():
                logger.handlers.clear()
                
            logger.addHandler(c_handler)
            logger.addHandler(f_handler)
            self.mlogger = logger
      
    def get(self):
        return self.mlogger