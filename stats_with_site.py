import re
import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver
import time
from selenium.webdriver import DesiredCapabilities
from selenium.webdriver.common.by import By
import json
from selenium.webdriver.common.keys import Keys


def set_config():
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    # service = ChromeService(ChromeDriverManager(version="108.0.5359.98").install())
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    # driver = webdriver.Chrome(service=service, options=chrome_options, desired_capabilities=d)
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=d)
    return driver


def stats_now(names):
    driver = set_config()
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    # url = "https://tracker.gg/valorant"
    # driver.get(url=url)
    # time.sleep(5)
    # accept = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    # time.sleep(2)
    #
    # find_account = driver.find_element(By.CLASS_NAME, 'search-box__bar').click()
    # time.sleep(3)
    #
    # input_name = driver.find_element(By.CSS_SELECTOR, 'input[data-v-885f6ad5]')
    # input_name.send_keys(name)
    # time.sleep(2)
    #
    # # з цим це не працює
    # # chrome_options.add_argument("--headless")
    # account = driver.find_element(By.CLASS_NAME, 'result-set__results').click()
    # time.sleep(3)

    new = []
    separator = ""
    for i in names:
        if i == " ":
            new.append(i.replace(' ', '%20'))
        else:
            new.append(i)
    s = separator.join(new)

    url = "https://tracker.gg/valorant/profile/riot/" + f"{s.replace('#', '%23')}/" + "overview"
    driver.get(url=url)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    time.sleep(3)

    new_titles = []
    name = []
    for title in soup.find_all("div", class_="stat align-left giant expandable"):
        value_span = title.find("span", class_="value")
        qwert = title.find("span", class_="name")

        new_titles.append(value_span.text)
        name.append(qwert.text)

    stats_dict = dict(zip(name, new_titles))
    driver.quit()

    with open(f'{names}.json', 'w') as f:
        json.dump(stats_dict, f)


def stats_all(names):
    driver = set_config()
    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    new = []
    separator = ""
    for i in names:
        if i == " ":
            new.append(i.replace(' ', '%20'))
        else:
            new.append(i)
    s = separator.join(new)

    url = "https://tracker.gg/valorant/profile/riot/" + f"{s.replace('#', '%23')}/" + "overview?season=all"
    driver.get(url=url)

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')
    new_titles = []
    name = []
    for title in soup.find_all("div", class_="stat align-left giant expandable"):
        value_span = title.find("span", class_="value")
        qwert = title.find("span", class_="name")

        new_titles.append(value_span.text)
        name.append(qwert.text)

    stats_dict = dict(zip(name, new_titles))
    driver.quit()

    with open(f'{names}.json', 'w') as f:
        json.dump(stats_dict, f)


def stats_last_game(names):
    d = DesiredCapabilities.CHROME
    d['loggingPrefs'] = {'browser': 'ALL'}
    # service = ChromeService(ChromeDriverManager(version="108.0.5359.98").install())
    chrome_options = webdriver.ChromeOptions()
    prefs = {"profile.default_content_setting_values.notifications": 2}
    chrome_options.add_experimental_option("prefs", prefs)
    chrome_options.add_experimental_option("detach", True)
    chrome_options.add_argument("--incognito")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(options=chrome_options, desired_capabilities=d)

    headers = {
        "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

    new = []
    separator = ""
    for i in names:
        if i == " ":
            new.append(i.replace(' ', '%20'))
        else:
            new.append(i)
    s = separator.join(new)

    url = "https://tracker.gg/valorant/profile/riot/" + f"{s.replace('#', '%23')}/" + "matches"
    driver.get(url=url)
    # driver.maximize_window()
    time.sleep(3)
    # accept = driver.find_element(By.ID, 'onetrust-accept-btn-handler').click()
    # time.sleep(1)

    soup = BeautifulSoup(driver.page_source, 'lxml')
    driver.find_element(By.TAG_NAME, 'body').send_keys(Keys.PAGE_DOWN * 1)
    time.sleep(1)


    title = ['Режим', 'Карта', 'Score1', 'Score2', 'Tracker Score', 'K/D/A', 'K/D', 'Детальніша статистика']
    data = []


    # kd = driver.find_element(By.CSS_SELECTOR, '#app > div.trn-wrapper > div.trn-container > div > main > div.container > div > div > div.sticky.top-0.z-10 > div.trn-match-drawer__tabs > div:nth-child(2)').click()
    # print(kd.text)
    # time.sleep(2)

    for i in soup.find_all("div", class_="trn-gamereport-list__group-entries"):
        regime = i.find("div", class_="trn-match-row__text-label")
        maps = i.find("div", class_="trn-match-row__text-value")
        score1 = i.find("span", class_="text-increment")
        score2 = i.find("span", class_="text-decrement")
        trs = i.find("div", class_="font-medium text-20 text-primary")
        kda = i.find("div", class_="trn-match-row__block min-w-24")

        data.append(regime.text)
        data.append(maps.text)
        data.append(score1.text)
        data.append(score2.text)
        data.append(trs.text)
        data.append(kda.text)

    stats_dict = dict(zip(title, data))

    string = str(stats_dict['Режим'])
    res = string.split('•')[0].strip()
    stats_dict['Режим'] = res

    string2 = str(stats_dict['K/D/A'])
    res2 = re.search(r'\d+ / \d+ / \d+', string2).group(0)
    stats_dict['K/D/A'] = res2
    
    parts = res2.split("/")
    kd = int(parts[0].strip()) / int(parts[1].strip())
    rounded_kd = round(kd, 1)
    formatted_kd = "{:.1f}".format(rounded_kd)
    stats_dict['K/D'] = formatted_kd

    stats_dict['Детальніша статистика'] = url
    
    print(stats_dict)
    driver.quit()

    with open(f'{names}.json', 'w') as f:
        json.dump(stats_dict, f)

