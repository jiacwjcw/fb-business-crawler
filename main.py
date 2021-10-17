from logging import log
import logging
import time
import datetime

from pages.login_page import LoginPage
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from utils.helper import *
from utils.config_helper import *
from pages.login_page import LoginPage

# chrome_options = Options()
# chrome_options.add_experimental_option("detach", True)


# log_filename = datetime.datetime.now().strftime("%Y-%m-%d_%H_%M_%S.log")
log_filename = "test.log"
logging.basicConfig(level=logging.INFO, filename=log_filename, filemode='w',
                    #format='[%(levelname).1s %(asctime)s] %(message)s',
                    format='[%(levelname)1.1s %(asctime)s %(module)s:%(lineno)d] %(message)s',
                    datefmt='%Y%m%d %H:%M:%S',
                    )

get_chrome_driver()
driver = webdriver.Chrome('./venv/bin/chromedriver')
revenue_host = ConfigHelper().get_revenue_host()

driver.get(revenue_host)
load_cookie(driver, './cookie')
driver.get(revenue_host)

login_page = LoginPage(driver)

if login_page.is_able_to_login():
    login_page.input_account(ConfigHelper().get_fb_account())
    login_page.input_password(ConfigHelper().get_fb_password())
    login_page.click_login_button()
    time.sleep(60)
    save_cookie(driver, './cookie')
    print("Save cookie!")
else:
    logging.info("ALREADY LOGIN!")

driver.close()
