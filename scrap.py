'''
HTML RESPONSE CODES

Informational responses (100–199),
Successful responses (200–299),
Redirects (300–399),
Client errors (400–499),
and Server errors (500–599).

'''
from bs4 import BeautifulSoup
import requests
import csv


url = "http://books.toscrape.com/"

page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")
section = soup.select("section div ol li")

for x in section:
    print("{}".format(x.h3.a.get("title")))
    print("{}{}".format(url, x.select_one(".thumbnail")["src"]))
    print("{}".format(x.select_one(".price_color").text.replace("Â", "")))