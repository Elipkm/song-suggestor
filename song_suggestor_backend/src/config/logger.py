

from datetime import datetime
import logging

def create_logger(filename):
    logger = logging.getLogger()
    datetime_now = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    log_file_name = filename + datetime_now + ".log"

    file_handler = logging.FileHandler("logs/" + log_file_name)
    console_handler = logging.StreamHandler()

    # Set levels for handlers
    level = "INFO"
    file_handler.setLevel(level)
    console_handler.setLevel(level)
    logger.setLevel(level)

    # Create formatters and add them to handlers
    formatter = logging.Formatter('%(levelname)s - %(message)s')
    file_handler.setFormatter(formatter)
    console_handler.setFormatter(formatter)
    # Add handlers to the logger
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)
    return logger