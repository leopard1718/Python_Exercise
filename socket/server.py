# -.- coding:utf-8 -.-
'''
Created on 2011-11-19

@author: icejoywoo
'''
import socket
import datetime

# 初始化socket
s = socket.socket()
# 获取主机名, 也可以使用localhost
# host = socket.gethostname()
host = "localhost"
# 默认的http协议端口号
port = 80

# 绑定服务器socket的ip和端口号
s.bind((host, port))

# 服务器名字/版本号
server_name = "MyServerDemo/0.1"

# 缓存时间, 缓存一天
expires = datetime.timedelta(days=1)
# GMT时间格式
GMT_FORMAT = '%a, %d %b %Y %H:%M:%S GMT'
# 相应网页的内容
content = '''
<html>
<head><title>MyServerDemo/0.1</title></head>
<body>
<h1>Hello, World!</h1>
<h2>你是SB吗？</h2>
</body>
</html>
'''

# 可同时连接五个客户端
s.listen(5)

# 提示信息
print "You can see a HelloWorld from this server in ur browser, type in", host, "\r\n"

# 服务器循环
while True:
    # 等待客户端连接
    c, addr = s.accept()
    print "Got connection from", addr, "\r\n"

    # 显示请求信息
    print "--Request Header:"
    # 接收浏览器的请求, 不作处理
    data = c.recv(1024)
    print data

    # 获得请求的时间
    now = datetime.datetime.utcnow()

    # 相应头文件和内容
    response = '''HTTP/1.1 200 OK
Server: %s
Date: %s
Expires: %s
Content-Type: text/html;charset=utf8
Content-Length: %s
Connection: keep-alive

%s''' % (
        server_name,
        now.strftime(GMT_FORMAT),
        (now + expires).strftime(GMT_FORMAT),
        len(content),
        content
    )
    # 发送回应
    c.send(response)
    print "--Response:\r\n", response
    c.close()
