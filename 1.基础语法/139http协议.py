# ### http协议
'''
基于tcp/ip

基于请求 响应模式

无状态保存

无连接





'''


'''
url : https://www.bilibili.com/video/BV1q7411T7N7?p=172

协议 ip(浏览器默认端口是80) 路径 ? 参数1 & 参数2(利用=) 
enc=utf-8 设置字符集

请求信息的格式
post 方法
-------------------------
方法   url   协议版本
post /from/entry http/1.1

请求首部字段


内容实体
-------------------------
get 方法
-------------------------
方法   url内容 协议版本

请求首部字段

-------------------------

# 响应格式
协议版本   状态码   状态码的原因短语
响应首部字段

主体

响应状态码
状态码的值 是当前客户端向服务器端发送请求时，返回的请求结果
1XX informational(信息性状态码) 接受的请求正在处理
2XX success(成功状态码) 请求正常处理完毕
3XX redirection(重定向状态码) 需要进行附加操作以完成请求
4XX client error(客户端错误状态码) 服务器无法处理请求
5XX server error(服务器错误状态码) 服务器处理请求出错










'''