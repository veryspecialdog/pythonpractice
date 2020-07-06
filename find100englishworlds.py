import requests
from lxml import etree

url ='https://movie.douban.com/chart'
header = {"User Agent":'Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:78.0) Gecko/20100101 Firefox/78.0'}
html = requests.get(url).content.decode('utf-8')
print(html)

