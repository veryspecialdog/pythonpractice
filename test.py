import requests
from lxml import etree

url ='https://movie.douban.com/top250'
html = requests.get(url).content.decode('utf-8')
print(html)
