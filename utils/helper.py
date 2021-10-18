import re
from datetime import datetime
from webdrivermanager import ChromeDriverManager as gc
from pickle5 import pickle


def save_cookie(driver, path):
    with open(path, 'wb') as filehandler:
        pickle.dump(driver.get_cookies(), filehandler)


def load_cookie(driver, path):
    with open(path, 'rb') as cookiesfile:
        cookies = pickle.load(cookiesfile)
        for cookie in cookies:
            driver.add_cookie(cookie)


def get_chrome_driver():
    gc().download_and_install()


def get_regex_time(time):
    return datetime.strptime(time, '%Y年%m月%d日').strftime('%Y-%m-%d')


def get_start_time_from_schedule(schedule_date: str):
    start_time = schedule_date.split(" – ")[0]
    return get_regex_time(start_time)


def get_regex_ad_name(ad_name: str):
    s = ad_name.split()[1]
    return re.sub(r'-(\d\d)~(\d\d)Y_[內|外]', '', s)


def get_regex_ad_cost(ad_cost: str):
    s = ad_cost.strip("NT$")
    s = re.sub(r',', "", s)
    return int(s)
