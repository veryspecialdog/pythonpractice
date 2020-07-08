import requests
from lxml import etree

url ='https://maoyan.com/films?catId=3&showType=3'
html = requests.get(url).content.decode('utf-8')
print(html)
