import logging
from datetime import datetime
import os

LOG_DIR = "logs"

def get_log_file_name():
    return f"log_{datetime.now().strftime('%Y-%m-%d')}.log"

LOG_FILE_NAME=get_log_file_name()
os.makedirs(LOG_DIR, exist_ok = True)

LOG_FILE_PATH = os.path.join(LOG_DIR,
                             LOG_FILE_NAME)

FORMAT = '%(asctime)s %(levelname)s %(message)s'

logging.basicConfig(filename = LOG_FILE_PATH, filemode = "w",
                    format = FORMAT, level = logging.INFO)