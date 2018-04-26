# coding=<encoding name> 例如，可添加# coding=utf-8

# 查询快递最上层的订单状态

import requests

url = 'http://www.kuaidi.com/index-ajaxselectcourierinfo-123456789-jd.html'
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
}           # get 请求的headers只需要加 "User-Agent"

r = requests.session()
rq = r.get(url,headers= headers,verify = False)
result = rq.json()

# 获取result结果中的data 数据
data1 = result ["data"]
print data1[0]
getresult = data1[0]["context"]
time = data1[0]["time"]
print  time
print getresult
if u'已签收' in getresult :
    print "快递已签收，记得取件哦"
else:
    print "快递还未送达，请耐心等待！"





