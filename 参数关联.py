# coding=<encoding name> 例如，可添加# coding=utf-8
import requests
import re
import json

# 登录
url = "https://passport.cnblogs.com/user/signin"

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

#  登录的参数
payload = {
"input1":"Kfp66w4G1K4C7i/htmVXqZgdwj4jGR3we1Q9z6FNx82FDIpwHXL4flzirtubZTOAPHQ2W6J4jEbwxaj7iDQx7VfriDV7rw3R2JLwcEGKkgxzYCaOW2uKrFeHSqyiW3rd9fuEvpuwDDEHdpww4JF4oEG1jAbigD+YH1kbDbnhWto=",
"input2":"p8C/M9D/ZcxQXPg3IzWicCB6PQLX+RHDJQ/mR25peQsWuVD6e87Tgtzc7Ju03BtNLpdVX1EEJwnRFMgDD7Kx6Iw3bx7WW80Ym4tKwfnFY52w28bymeTZFHoThASQNdBSu+aBOIUyOORYS3tl0SvaEY6DCRxM6GOSzR/aq6NUR88=",
"remember":True}

s = requests.session()
r = s.post(url, json=payload, headers=headers,verify=False)
print r.json()

# 保存草稿箱
url2= "https://i.cnblogs.com/EditPosts.aspx?opt=1"
body = {"__VIEWSTATE": "",
        "__VIEWSTATEGENERATOR":"FE27D343",
        "Editor$Edit$txbTitle":"参数关联！！！！",
        "Editor$Edit$EditorBody":"加油加油加油，15  15  15 进步，加油",
        "Editor$Edit$Advanced$ckbPublished":"on",
        "Editor$Edit$Advanced$chkDisplayHomePage":"on",
        "Editor$Edit$Advanced$chkComments":"on",
        "Editor$Edit$Advanced$chkMainSyndication":"on",
        "Editor$Edit$lkbDraft":"存为草稿",
         }
r2 = s.post(url2, data=body, verify=False)
print r.content
# 用正则表达式提取参数（文章ID）
geturl = r2.url
# 正则表达式切割提取 id参数
articleid = re.findall(r"postid=(.+?)&",geturl)
print articleid
print articleid[0]
# 删除发的稿

# 删除发稿的URL
url3 = "https://i.cnblogs.com/post/delete"
# 也就是说保存草稿箱成功之后，重定向一个url地址，里面带有postId这个参数
# 文章的ID 参数 字典

json3 = {"postid":articleid[0]}
rq3 = s.post(url3,json = json3,verify = False)
print rq3.json()



