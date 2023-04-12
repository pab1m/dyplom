import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.common.by import By
# from webdriver_manager.chrome import ChromeDriverManager


def set_config():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    # service = ChromeService(ChromeDriverManager(version="108.0.5359.98").install())
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    # chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(service=service, options=chrome_options, desired_capabilities=d)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=d)
    return driver

driver = set_config()

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

name = str(input("Enter name: "))
time.sleep(3)


url = "https://tracker.gg/valorant"

driver.get(url=url)
time.sleep(5)

accept = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
time.sleep(2)

find_account = driver.find_element(By.CLASS_NAME, 'search-box__bar').click()
time.sleep(3)

input_name = driver.find_element(By.CSS_SELECTOR, 'input[data-v-885f6ad5]')
input_name.send_keys(name)
time.sleep(5)

#з цим це не працює

# chrome_options.add_argument("--headless")
account = driver.find_element(By.CLASS_NAME, 'result-set__results').click()
time.sleep(3)

new = []
separator = ""

for i in name:
    if i == " ":
        new.append(i.replace(' ', '%20'))
    else:
        new.append(i)

s = separator.join(new)


url2 = "https://tracker.gg/valorant/profile/riot/" + f"{s.replace('#', '%23')}/" + "overview"
print(url2)



response = requests.get(url2, headers=headers)
soup = BeautifulSoup(response.content, 'lxml')


def stats_now():
    news_titles = []
    name = []
    for title in soup.find_all("div", class_="stat align-left giant expandable"):
        value_span = title.find("span", class_="value")
        qwert = title.find("span", class_="name")

        news_titles.append(value_span.text)
        name.append(qwert.text)

    stats_dict = dict(zip(name, news_titles))

    print(f"{name[0]}: {stats_dict[name[0]]} \n{name[1]}: {stats_dict[name[1]]} \n{name[2]}: {stats_dict[name[2]]} \n{name[3]}: {stats_dict[name[3]]}")

stats_now()

driver.quit()
