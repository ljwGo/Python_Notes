# 爬虫相关
import requests
'''
# 状态码
    200 ok
    404 link no find
    400 
'''

'''
# 基本语法
response = requests.get('http://www.baidu.com')
print(response)
# 获取状态吗
res = response.status_code
print(res)
# 获取网页中的字符编码
res = response.apparent_encoding
print(res)
# 设置编码集，防止乱码
response.encoding = res
# 获取网页当中的内容
res = response.text
print(res)
'''

#<!DOCTYPE html>
#<!--STATUS OK--><html> <head><meta http-equiv=content-type content=text/html;charset=utf-8><meta http-equiv=X-UA-Compatible content=IE=Edge><meta content=always name=referrer><link rel=stylesheet type=text/css href=http://s1.bdstatic.com/r/www/cache/bdorz/baidu.min.css><title>百度一下，你就知道</title></head> <body link=#0000cc> <div id=wrapper> <div id=head> <div class=head_wrapper> <div class=s_form> <div class=s_form_wrapper> <div id=lg> <img hidefocus=true src=//www.baidu.com/img/bd_logo1.png width=270 height=129> </div> <form id=form name=f action=//www.baidu.com/s class=fm> <input type=hidden name=bdorz_come value=1> <input type=hidden name=ie value=utf-8> <input type=hidden name=f value=8> <input type=hidden name=rsv_bp value=1> <input type=hidden name=rsv_idx value=1> <input type=hidden name=tn value=baidu><span class="bg s_ipt_wr"><input id=kw name=wd class=s_ipt value maxlength=255 autocomplete=off autofocus></span><span class="bg s_btn_wr"><input type=submit id=su value=百度一下 class="bg s_btn"></span> </form> </div> </div> <div id=u1> <a href=http://news.baidu.com name=tj_trnews class=mnav>新闻</a> <a href=http://www.hao123.com name=tj_trhao123 class=mnav>hao123</a> <a href=http://map.baidu.com name=tj_trmap class=mnav>地图</a> <a href=http://v.baidu.com name=tj_trvideo class=mnav>视频</a> <a href=http://tieba.baidu.com name=tj_trtieba class=mnav>贴吧</a> <noscript> <a href=http://www.baidu.com/bdorz/login.gif?login&amp;tpl=mn&amp;u=http%3A%2F%2Fwww.baidu.com%2f%3fbdorz_come%3d1 name=tj_login class=lb>登录</a> </noscript> <script>document.write('<a href="http://www.baidu.com/bdorz/login.gif?login&tpl=mn&u='+ encodeURIComponent(window.location.href+ (window.location.search === "" ? "?" : "&")+ "bdorz_come=1")+ '" name="tj_login" class="lb">登录</a>');</script> <a href=//www.baidu.com/more/ name=tj_briicon class=bri style="display: block;">更多产品</a> </div> </div> </div> <div id=ftCon> <div id=ftConw> <p id=lh> <a href=http://home.baidu.com>关于百度</a> <a href=http://ir.baidu.com>About Baidu</a> </p> <p id=cp>&copy;2017&nbsp;Baidu&nbsp;<a href=http://www.baidu.com/duty/>使用百度前必读</a>&nbsp; <a href=http://jianyi.baidu.com/ class=cp-feedback>意见反馈</a>&nbsp;京ICP证030173号&nbsp; <img src=//www.baidu.com/img/gs.gif> </p> </div> </div> </div> </body> </html>

url_lst = [
'http://www.4399.com',
'http://www.7k7k.com',
'http://www.taobao.com'
]

import time
import gevent
from gevent import monkey
def get_url(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(response.text)

# 1 正常爬取
'''
startime = time.time()
for i in url_lst:
    get_url(i)
endtime = time.time()
print(endtime - startime)
#0.2209491729736328
'''


startime = time.time()
lst = []
for i in url_lst:
    g = gevent.spawn(get_url,i)
    lst.append(g)
# 等待所有的协程任务执行完毕之后，再向下执行
gevent.joinall(lst)
endtime = time.time()
print(endtime - startime)
'''
在多任务中，在进程资源一定的情况下，线程数量一定的情况下，增加多协程
能够使资源最大化，抗住更大并发任务
'''