import requests
from lxml import etree

url ='http://www.mtime.com/top/movie/top100/'
html = requests.get(url).content.decode('utf-8')
print(html)
