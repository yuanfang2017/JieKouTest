# coding=<encoding name> 例如，可添加# coding=utf-8

# 获取重定向后的URL
import  requests

url = 'https://i.cnblogs.com/EditPosts.aspx?opt=1'

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0"
}
r = requests.session()
# allow_redirects=False 禁止重定向
rq = r.get(url ,headers =headers ,verify = False,allow_redirects=False)
print rq.status_code
geturl = rq.headers["location"]
print geturl


