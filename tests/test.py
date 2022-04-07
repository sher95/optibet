import time
import traceback
import pytest
from selenium.webdriver.common.by import By
from utilities.read_properties import read_Config
#from pages.BasePage import BasePage

#imdb = read_Config.get_url()  # If this line will give error, then just comment it and comment out line in the below
imdb = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"


@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass


class Test_End_to_End1(BaseTest):
    def test_add_movie_to_watchlist(self):
        self.driver.get(imdb)
        self.driver.implicitly_wait(5)
        time.sleep(60)
        add_button = self.driver.find_element(By.XPATH, '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[2]/td[5]/div/div')
        title = add_button.get_attribute("title")
        if title == "Click to add to watchlist":
            add_button.click()

        if title == "Click to remove from watchlist":
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_adding_own_rating(self):
        pass

    def test_sorting(self):
        pass
