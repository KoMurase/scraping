from bs4 import BeautifulSoup
from urllib.request import urlopen

target_url = "https://duet.doshisha.ac.jp/kokai/html/fi/fi050/FI05001G.html"

html = urlopen(target_url)
data = html.read()
html = data.decode('utf-8')

soup = BeautifulSoup(html, 'html.parser')

data = soup.select("#form1 > div:nth-child(10) > h3")
print(data)


#pagePath > ol > li:nth-of-type(1) > a
#form1 > div:nth-child(11) > div > span > table > tbody
#form1 > div:nth-child(11) > div > span > table > tbody > tr:nth-child(2) > td:nth-child(2)
