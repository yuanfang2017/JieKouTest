# coding=<encoding name> 例如，可添加# coding=utf-8
import requests
import re
# 定义一个登陆函数的功能,传三个参数，session 的对象，登陆密码参数，登陆URL
s = requests.session()
def login(s,url1,payload):
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 6.1; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
        "Accept-Encoding": "gzip, deflate, br",
        "Content-Type": "application/json; charset=utf-8",
        #"VerificationToken": "C6nkGGBPQ-RfrsDcIbMPAhY9GJY9tRpBPXVglIyGHRXRrBjrww3KZ-cqEX--nT5Qb39cSL5nR9lvQqjcHgwHxzg2g6g1:vjPmXS-Jk9u0430I8MFGNnW43vwjJxSBzqARTNK4_duDPeL9ZCw3cKPX5gU8bo4gGbCUijPzCJ1VZ4UTZQeATNkOY6Q1",
        "X-Requested-With": "XMLHttpRequest",
        # "Referer": "https://passport.cnblogs.com/user/signin?ReturnUrl=https%3A%2F%2Fwww.cnblogs.com%2F",
        "Content-Length": "386",
        "Cookie": "_ga=GA1.2.910041544.1500282182; _gid=GA1.2.1698048186.1500282182; SERVERID=9b2e527de1fc6430919cfb3051ec3e6c|1500364729|1500364712; ASP.NET_SessionId=i5zkri4gdr3iwcm4ljfw2pwz",
        "Connection": "keep-alive"}
    r = s.post(url1, json=payload, headers=headers, verify=False)
    result = r.json()
    print result
    # 返回结果，TRUE or FALSE
    return result['success']
# 定义保存到草稿箱的功能函数，传 ession 的对象,请求URL，标题，内容，
def save(s, url2 ,title,data_body):
    body = {"__VIEWSTATE": "",
            "__VIEWSTATEGENERATOR": "FE27D343",
            "Editor$Edit$txbTitle": title,
            "Editor$Edit$EditorBody": data_body,
            "Editor$Edit$Advanced$ckbPublished": "on",
            "Editor$Edit$Advanced$chkDisplayHomePage": "on",
            "Editor$Edit$Advanced$chkComments": "on",
            "Editor$Edit$Advanced$chkMainSyndication": "on",
            "Editor$Edit$lkbDraft": "存为草稿",
            }
    r2 = s.post(url2, data=body, verify=False)
    # 返回 重定向的地址
    return r2.url


# 定义一个提取正则表达式的函数的功能
def get_postid(u):
    articleid = re.findall(r"postid=(.+?)&",u)
    # 返回 得到的ID
    if len(articleid) > 1:
        return ''
    else:
        return articleid[0]

# 定义一个删除文章的功能函数，传参为传 ession 的对象，ID，URL
def delete_article(s,url3,postid1):
    jason3 = {"postid":postid1}
    r3 = s.post(url3,json =jason3,verify=False)
    print r3.json()
# main函数
if __name__ == '__main__':
    url1 = "https://passport.cnblogs.com/user/signin"
    payload ={
             "input1":"Kfp66w4G1K4C7i/htmVXqZgdwj4jGR3we1Q9z6FNx82FDIpwHXL4flzirtubZTOAPHQ2W6J4jEbwxaj7iDQx7VfriDV7rw3R2JLwcEGKkgxzYCaOW2uKrFeHSqyiW3rd9fuEvpuwDDEHdpww4JF4oEG1jAbigD+YH1kbDbnhWto=",
             "input2":"p8C/M9D/ZcxQXPg3IzWicCB6PQLX+RHDJQ/mR25peQsWuVD6e87Tgtzc7Ju03BtNLpdVX1EEJwnRFMgDD7Kx6Iw3bx7WW80Ym4tKwfnFY52w28bymeTZFHoThASQNdBSu+aBOIUyOORYS3tl0SvaEY6DCRxM6GOSzR/aq6NUR88=",
             "remember":True}
    login(s,url1,payload)
    url2 = "https://i.cnblogs.com/EditPosts.aspx?opt=1"
    u = save(s,url2,"哈哈哈哈哈哈哈哈","啦啦啦啦阿里啦啦啦阿拉啦")
    postid = get_postid(u)
    url3 = "https://i.cnblogs.com/post/delete"
    delete_article(s,url3,postid)



