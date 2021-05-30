from bs4 import BeautifulSoup
# import requests_html for rendering javascript pages as HTML
from requests_html import HTMLSession
#
# BeautifulSoup for parsing HTML rendered from requests_html

session = HTMLSession()
url = "http://www.gong-cha-sg.com/stores/"
r = session.get(url)
r.html.render(sleep=1, keep_page=True, scrolldown=1)

# stores stores the javascript rendered as HTML
# xpath - Inspect in Chrome, find parent container and copy XPATH
# //*[@id="asl-storelocator"]/div[3]/div[1]
stores = r.html.xpath('//*[@id="asl-storelocator"]/div[3]/div[1]', first=True).html

# Now send it to BeautifulSoup to parse the rendered HTML
soup = BeautifulSoup(stores, 'html.parser')
tags = soup.findAll('p', class_='p-title')
infolist = []
for tag in tags:
    info = tag.text
    infolist.append(info)

for i in infolist:
    print(i)

# Use below for non-JS rendered webpages

# r = requests.get(url)
# soup = BeautifulSoup(r.content, 'html.parser')
# tags = soup.findAll('div', class_='locator-location-basic')
# print(soup)

# info = []
# for tag in tags:
#     info.append(tag.text)
#
# print(info)
