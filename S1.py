import socket
import time


# 创建对象
sk = socket.socket()

# 绑定IP和端口
sk.bind(('127.0.0.1',8001))

# 监听
sk.listen()

def rihan(url):
    return '欢迎 日韩{}'.format(url)
def oumei(url):
    return '欢迎 欧美{}'.format(url)
def guochan(url):
    return '欢迎 国产{}'.format(url)
# 等待链接
def home(url):
    with open('home.html','r',encoding='utf-8') as f:
        res = f.read()
        return res
def timer(url):
    now = time.time()
    with open('time.html','r',encoding='utf-8') as f:
        res = f.read()
        return res.replace('@@time@@',str(now))


list = [
    ('/rihan',rihan),
    ('/oumei',oumei),
    ('/guochan',guochan),
    ('/home', home),
    ('/time', timer),
]


while True:
    conn,addr = sk.accept() #建立连接
    #接收数据
    data = conn.recv(2048).decode('utf-8')
    url = data.split()[1]
    #返回数据
    conn.send(b"HTTP/1.1 200 OK\r\ncontent-type: text/html; charset=utf-8\r\n\r\n")

    funn = None

    for i in list:
        if url == i[0]:
            funn = i[1]
            break
    if funn:
        res = funn(url)
    else:
        res = '404 not found'

    conn.send(res.encode('utf-8'))

    #断开连接
    conn.close()



