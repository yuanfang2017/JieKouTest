# coding=<encoding name> 例如，可添加# coding=utf-8
import requests
import urllib
from bs4 import BeautifulSoup
rg = requests.get('http://699pic.com/sousuo-218808-13-1.html')
rc = rg.content
# 解析为HTML
html = BeautifulSoup(rc,"html.parser")
imagelocation = html.find_all(class_="lazy")
# 获取对应的图片

for i in imagelocation:
    images = i["data-original"]
    title = i["title"]
    x = 0
    print images
    print title
    urllib.urlretrieve(images,'%s.jpg'% title)
    x = x+1
with open(os.getcwd()+"\\jpg\\"+title+'.jpg', "wb") as f:
19         f.write(requests.get(jpg_rl).content)






