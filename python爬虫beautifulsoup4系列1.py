# coding=<encoding name> 例如，可添加# coding=utf-8
from bs4 import BeautifulSoup
import requests
import json
rq = requests.get('http://www.cnblogs.com/yuanyuan2017/p/7137162.html')
rc = rq.content
# 解析HTML 页面
html = BeautifulSoup(rc,"html.parser")
title = html.find_all("title")
print title
print json.loads('"%s"' %title)





