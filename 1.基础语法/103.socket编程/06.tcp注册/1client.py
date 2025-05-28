# ### 客户端
import socket
import struct
import json
sk = socket.socket()
sk.connect(('127.0.0.2', 50000))

# 发送逻辑
def client_send(info,mode=False):
    b_info = json.dumps(info).encode('utf-8')
    if mode:
        sk.send(struct.pack('i', len(b_info)))
    sk.send(b_info)

# 接受逻辑
def client_recv(mode=False, len_tup=1024):
    if mode:
        # 真实信息长度
        len_tup = struct.unpack('i', sk.recv(4))
    b_info = sk.recv(len_tup).decode('utf-8')
    # 获取字典
    return json.loads(b_info)

def register():
    account = input('请输入您的账号:')
    password1 = input('请输入您的密码:')
    password2 = input('请确认您的密码:')
    info_dic = {'account': account, 'password1': password1, 'password2': password2, 'operate': 'regiser'}
    client_send(info_dic)
    # info = client_recv()

def login():
    account = input('请输入您的账号:')
    password = input('请输入您的密码:')
    info_dic = {'account': account, 'password': password, 'operate': 'login'}
    client_send(info_dic)

def myexit(none):
    client_send({'operate': 'myexit'})
    exit('欢迎下次登录')

def view(operate_dic):
    for num, tup in enumerate(operate_dic, start=1):
        print(num + tup[0])

def download(filename):
    client_send({'filename': filename, 'operate': 'download'})
    filename = os.path.join(os.get(), 'file')
    os.mkdir(filename)
    filename2 = os.path.join(filename,'download.html')
    with open(filename2,mode='wb') as fp:
            while True:



operate_dic1 = {'注册': register, '登录': login, '退出': myexit}
operate_dic2 = {'下载': download, '退出': myexit}

def main():
    while True:
        view(operate_dic1)
        choice = int(input('请选择你要执行的操作:'))
        operate_dic1[choice-1]()
        respond = client_recv()
        print(respond['respond'])
        if respond['result']:
            while True:
                view(operate_dic2)
                choice2 = int(input('请选择你要执行的操作:'))
                operate_dic2[choice2-1]('###')
                # server_recv()

# 关闭客户端
sk.close()