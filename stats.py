import requests
from bs4 import BeautifulSoup
import lxml
from selenium import webdriver


headers = {"user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36"}

# option = webdriver.ChromeOptions
# option.add_argument("user-agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36")


def stats_now(url):

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    news_titles = []
    name = []

    for title in soup.find_all("div", class_="stat align-left giant expandable"):
        value_span = title.find("span", class_="value")
        qwert = title.find("span", class_="name")

        news_titles.append(value_span.text)
        name.append(qwert.text)

    stats_dict = dict(zip(name, news_titles))

    print(f"{name[0]}: {stats_dict[name[0]]} \n{name[1]}: {stats_dict[name[1]]} \n{name[2]}: {stats_dict[name[2]]} \n{name[3]}: {stats_dict[name[3]]}")


def stats_all(url):

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'lxml')

    news_titles = []
    name = []

    for title in soup.find_all("div", class_="stat align-left giant expandable"):
        value_span = title.find("span", class_="value")
        qwert = title.find("span", class_="name")

        news_titles.append(value_span.text)
        name.append(qwert.text)

    stats_dict = dict(zip(name, news_titles))

    print(f"{name[0]}: {stats_dict[name[0]]} \n{name[1]}: {stats_dict[name[1]]} \n{name[2]}: {stats_dict[name[2]]} \n{name[3]}: {stats_dict[name[3]]}")

print("Статистика за цей акт")
stats_now("https://tracker.gg/valorant/profile/riot/Pab1m%231606/overview")
print(f"\nСтатистика за весь час")
stats_all("https://tracker.gg/valorant/profile/riot/Pab1m%231606/overview" + "?season=all")