import time
import traceback
import pytest
from selenium.webdriver.common.by import By
from utilities.read_properties import read_Config


imdb = read_Config.get_url()  # If this line will give error, then just comment it and comment out line in the below
signing = read_Config.get_signing_url()


# imdb = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"
# signing = "https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20"

@pytest.mark.usefixtures("chrome_setup")
class BaseTest:
    pass


class Test_imdb(BaseTest):

    def test_login(self):
        self.driver.get(signing)
        time.sleep(3)  # used time not implicity_wait because of asking for enter code from image
        self.driver.find_element(By.ID, "ap_email").send_keys("sher95c@gmail.com")
        self.driver.find_element(By.ID, "ap_password").send_keys("optibet!@")
        self.driver.find_element(By.ID, "signInSubmit").click()

    def test_add_movie_to_watchlist(self):
        time.sleep(3)
        self.driver.get(imdb)
        self.driver.implicitly_wait(5)
        add_button = self.driver.find_element(By.CSS_SELECTOR,
                                              "#main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.watchlistColumn > div > div")
        time.sleep(2)
        title_before = add_button.get_attribute("title")
        if title_before == "Click to add to watchlist":
            add_button.click()
        time.sleep(2)
        add_button = self.driver.find_element(By.CSS_SELECTOR,
                                              "#main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.watchlistColumn > div > div")
        title_after = add_button.get_attribute("title")
        if title_after == "Click to remove from watchlist":
            assert True
        else:
            traceback.format_exc()
            assert False

    def test_adding_own_rating(self):
        self.driver.implicitly_wait(5)
        self.driver.find_element(By.CLASS_NAME, "unseen").click()
        self.driver.find_element(By.XPATH,
                                 '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[4]/div/div[1]/div/ol/li[8]').click()
        time.sleep(3)
        rate = self.driver.find_element(By.XPATH, "//div[@class='rating']")
        t = rate.text
        if t == "8":
            assert True
        else:
            assert False

    def test_sorting(self):
        self.driver.find_element(By.ID, "lister-sort-by-options").click()
        time.sleep(2)
        self.driver.find_element(By.CSS_SELECTOR, "#lister-sort-by-options > option:nth-child(2)").click()  # IMDB
        self.driver.find_element(By.CSS_SELECTOR,
                                 "#lister-sort-by-options > option:nth-child(3)").click()  # Release Date
        time.sleep(2)
        sort = self.driver.find_element(By.XPATH,
                                        '//*[@id="main"]/div/span/div/div/div[3]/table/tbody/tr[1]/td[3]/strong')
        t = sort.text
        if t != "9":
            assert True
        else:
            assert False
