import requests
from lxml import etree

url ='https://maoyan.com/films?catId=3&sourceId=2&yearId=15&showType=3'
header = {"User Agent":'Mozilla/5.0 (iPhone; CPU iPhone OS 13_2_3 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.3 Mobile/15E148 Safari/604.1'}
html = requests.get(url,headers=header).content.decode('utf-8')
print(html)