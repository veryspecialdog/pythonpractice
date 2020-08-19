import requests
import re


path = r'C:\Users\Administrator\Documents\GitHub\pythonpractice '

url = "http://pic.netbian.com/4kmeinv/index.html"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.1 (KHTML, like Gecko) Chrome/21.0.1180.89 Safari/537.1",
    "Referer": "http://pic.netbian.com/4kmeinv/index.html"
}


response = requests.get(url, headers=headers)


response.encoding = 'GBK'


img_info = re.findall('img src="(.*?)" alt="(.*?)" /', response.text)

for src, name in img_info:
    img_url = 'http://pic.netbian.com' + src   
    img_content = requests.get(img_url, headers=headers).content
    img_name = name + '.jpg'
    with open(path + img_name, 'wb') as f:     
        print(f"正在为您下载图片：{img_name}")
        f.write(img_content)