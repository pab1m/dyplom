import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities
from undetected_chromedriver import ChromeDriverManager


def set_config():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    # service = ChromeService(ChromeDriverManager(version="107.0.5304.18").install())
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=d)
    return driver

driver = set_config()





# driver_path = "chromedriver"




driver.get("https://www.google.com")

time.sleep(5000)

driver.quit()



# option = webdriver.ChromeOptions
# option.add_argument("user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")
#
#
#
#
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.content, 'lxml')
#
# news_titles = []
# name = []
#
# for title in soup.find_all("div", class_="stat align-left giant expandable"):
#     value_span = title.find("span", class_="value")
#     qwert = title.find("span", class_="name")
#
#     news_titles.append(value_span.text)
#     name.append(qwert.text)
#
# stats_dict = dict(zip(name, news_titles))
#
# print(f"{name[0]}: {stats_dict[name[0]]} \n{name[1]}: {stats_dict[name[1]]} \n{name[2]}: {stats_dict[name[2]]} \n{name[3]}: {stats_dict[name[3]]}")
#
