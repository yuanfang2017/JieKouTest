# coding=<encoding name> 例如，可添加# coding=utf-8
# 导包
import  requests
# 用get 方法 就能访问一个地址
r = requests.get('https://www.cnblogs.com/')
# 获取状态码
# print r.status_code
# 获取响应的内容
# print r.content
# 再发一个带参数的get请求
# 定义一个字典，接收传的参数
# 多个参数格式：{"key1": "value1", "key2": "value2", "key3": "value3"}
parm = {"t":"b","w":"java"}
y = requests.get('http://zzk.cnblogs.com/',params=parm)
print y.status_code
print y.content

