import time
import traceback
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

driver.maximize_window()
signing = "https://www.imdb.com/ap/signin?openid.pape.max_auth_age=0&openid.return_to=https%3A%2F%2Fwww.imdb.com%2Fregistration%2Fap-signin-handler%2Fimdb_us&openid.identity=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.assoc_handle=imdb_us&openid.mode=checkid_setup&siteState=eyJvcGVuaWQuYXNzb2NfaGFuZGxlIjoiaW1kYl91cyIsInJlZGlyZWN0VG8iOiJodHRwczovL3d3dy5pbWRiLmNvbS8_cmVmXz1sb2dpbiJ9&openid.claimed_id=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0%2Fidentifier_select&openid.ns=http%3A%2F%2Fspecs.openid.net%2Fauth%2F2.0&tag=imdbtag_reg-20"
imdb = "https://www.imdb.com/chart/top/?ref_=nv_mv_250"

driver.get(signing)
driver.find_element(By.ID, "ap_email").send_keys("sher95c@gmail.com")
driver.find_element(By.ID, "ap_password").send_keys("optibet!@")
driver.find_element(By.ID, "signInSubmit").click()
time.sleep(500)



driver.get(imdb)
time.sleep(10)
driver.implicitly_wait(5)
#time.sleep(60)
add_button = driver.find_element(By.CSS_SELECTOR, '#main > div > span > div > div > div.lister > table > tbody > tr:nth-child(1) > td.watchlistColumn > div > div')
title = add_button.get_attribute("title")
print(title)
time.sleep(10)
add_button.click()
title = add_button.get_attribute("title")
print(title)

