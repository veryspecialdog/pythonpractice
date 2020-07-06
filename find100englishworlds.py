import requests
from lxml import etree

url ='https://maoyan.com/films?catId=3&sourceId=2&yearId=15&showType=3'
header = {"User Agent":'Mozilla/5.0 (Windows NT 10.0;Win64;x64;rv:78.0) Gecko/20100101 Firefox/78.0'}
html = requests.get(url,headers=header).content.decode('utf-8')
