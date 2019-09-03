import requests
from bs4 import BeautifulSoup
import re

res = requests.get("https://edition.cnn.com/2018/04/27/politics/us-flies-bombers-south-china-sea/index.html")
res.encoding = 'utf-8'
soup = BeautifulSoup(res.text, "html.parser")
title = soup.title
#date = soup.find_all('meta', itemprop='datePublished')
date = soup.find_all('p', {'class': re.compile('update-time')})
#print(soup.prettify())
print(title)
print(date)