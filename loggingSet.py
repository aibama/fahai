import logging  
import logging.config  
import sys, os
logging.config.fileConfig(r"C:\Users\Administrator\PycharmProjects\fahai\logging.conf")    # 采用配置文件

# create logger  
logger = logging.getLogger("simpleExample")

# "application" code  
logger.debug("debug message")  
logger.info("info message")  
logger.warn("warn message")  
logger.error("error message")  
logger.critical("critical message")