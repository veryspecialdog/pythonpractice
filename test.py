import requests
from lxml import etree

url ='https://maoyan.com/board/4'
html = requests.get(url).content.decode('utf-8')
print(html)

    
    