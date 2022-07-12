import logging

logging.basicConfig(level=logging.INFO)

api_logger = logging.getLogger('api')
file_logger = logging.getLogger('file')

api_handler = logging.FileHandler('logs/api.log')
file_handler = logging.FileHandler('logs/files.log')

formatter = logging.Formatter("%(asctime)s [%(levelname)s] %(message)s")
api_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

api_logger.addHandler(api_handler)
file_logger.addHandler(file_handler)
