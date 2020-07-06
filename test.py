import requests
from lxml import etree

url ='https://home.firefoxchina.cn/'
html = requests.get(url).content.decode('utf-8')
print(html)