import inspect
import logging
#import allure


def custom_logging():
    logger_name = inspect.stack()[1][3]

    logger = logging.getLogger(logger_name)
    logger.setLevel(logging.DEBUG)

    file_handler = logging.FileHandler("../reports/optibetTest.log", mode='a')
    file_handler.setLevel(logging.DEBUG)

    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelName)s : %(message)s', datefmt='%d/%m/%y %I:%M:%S %p %A')

    file_handler.setFormatter(formatter)
    logger.addHandler(file_handler)

    return logger


"""def allure_logs(text):
    with allure.step(text):
        pass"""