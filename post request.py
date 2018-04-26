# coding=<encoding name> 例如，可添加# coding=utf-8
# 导包
import requests

# 定义一个字典传入参数
r = {"t":"b","w":"java"}

# post请求
rq = requests.get('http://zzk.cnblogs.com/',data = r)
print rq.status_code
print (rq.text)



