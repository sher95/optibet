import time
import traceback
import pytest
from selenium.webdriver.common.by import By
from Utilities.read_properties import read_Config

calculator = read_Config.get_url()  # If this line will give error, then just comment it and comment out line in the below
# calculator = "http://juliemr.github.io/protractor-demo/"


@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass


class Test_End_to_End1(BaseTest):
    def open_page(self):
        pass
