# coding=<encoding name> 例如，可添加# coding=utf-8
# 自动登录博客园
import requests
import json
import urllib2
from requests.packages.urllib3.exceptions import InsecureRequestWarning
# 禁用安全请求警告
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
se = requests.session()
# 登录的URL
url = 'https://passport.cnblogs.com/user/signin'
# 请求头 header，抓包得的
headers = {
"User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
"Accept": "application/json, text/javascript, */*; q=0.01",
"Accept-Language":"zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
"Accept-Encoding": "gzip, deflate, br",
"Content-Type": "application/json; charset=utf-8",
# "VerificationToken": "C6nkGGBPQ-RfrsDcIbMPAhY9GJY9tRpBPXVglIyGHRXRrBjrww3KZ-cqEX--nT5Qb39cSL5nR9lvQqjcHgwHxzg2g6g1:vjPmXS-Jk9u0430I8MFGNnW43vwjJxSBzqARTNK4_duDPeL9ZCw3cKPX5gU8bo4gGbCUijPzCJ1VZ4UTZQeATNkOY6Q1",
"X-Requested-With": "XMLHttpRequest",
# "Referer": "https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F",
"Content-Length": "386",
"Cookie": "_ga=GA1.2.910041544.1500282182; _gid=GA1.2.1698048186.1500282182; SERVERID=9b2e527de1fc6430919cfb3051ec3e6c|1500364729|1500364712; ASP.NET_SessionId=i5zkri4gdr3iwcm4ljfw2pwz",
"Connection": "keep-alive"}

# 传入参数字典格式
r = {
"input1":"Kfp66w4G1K4C7i/htmVXqZgdwj4jGR3we1Q9z6FNx82FDIpwHXL4flzirtubZTOAPHQ2W6J4jEbwxaj7iDQx7VfriDV7rw3R2JLwcEGKkgxzYCaOW2uKrFeHSqyiW3rd9fuEvpuwDDEHdpww4JF4oEG1jAbigD+YH1kbDbnhWto=",
"input2":"p8C/M9D/ZcxQXPg3IzWicCB6PQLX+RHDJQ/mR25peQsWuVD6e87Tgtzc7Ju03BtNLpdVX1EEJwnRFMgDD7Kx6Iw3bx7WW80Ym4tKwfnFY52w28bymeTZFHoThASQNdBSu+aBOIUyOORYS3tl0SvaEY6DCRxM6GOSzR/aq6NUR88=",
"remember":False}

# 发起请求
rq = se.post(url,json = r,headers = headers,verify=False,allow_redirects=False)
print (rq.status_code)
print (rq.content.decode())
followeespage = urllib2.urlopen("http://home.cnblogs.com/followees/")
followeespagecontent = followeespage.read().decode("utf8")
print followeespagecontent