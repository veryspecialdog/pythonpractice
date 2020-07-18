import requests
from lxml import etree

url='https://music.douban.com'
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
html=requests.get(url,headers =headers)
print(html)

    
    