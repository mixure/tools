import logging
from logging.handlers import RotatingFileHandler
from config import config

log_dir=config.Path.log_dir

logger=logging.getLogger()
logger.setLevel(logging.DEBUG)
file_handler=RotatingFileHandler('%s/log' %log_dir,maxBytes=1024*1024,
                backupCount=3)
file_handler.setFormatter(logging.Formatter("%(asctime)s %(msg)s"))
file_handler.setLevel(logging.DEBUG)
logger.addHandler(file_handler)

console_handler=logging.StreamHandler()
console_handler.setFormatter(logging.Formatter("%(asctime)s %(msg)s"))
console_handler.setLevel(logging.DEBUG)
logger.addHandler(console_handler)
