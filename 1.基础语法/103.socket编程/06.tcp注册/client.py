import socket
import json
sk = socket.socket()
sk.connect(('127.0.0.1',9004))
# 处理收发数据的逻辑
def auth(opt):
    usr = input('username:').strip()
    pwd = input('password:').strip()
    dic = {'user':usr,'pwd':pwd,'operate':opt}
    strvar = json.dumps(dic)
    # 把数据发送给服务端
    sk.send(strvar.encode())
    str_info = sk.recv(1024).decode()
    return json.loads(str_info)

operate_dic1 = [('登录','login'),('注册','register'),('退出','myexit')]
operate_dic2 = [('下载','download'),('上传','dump')]

def main(operate_dic):
    for i, tup in enumerate(operate_dic, start=1):
        print(i, tup[1])
    num = int(input('请输入您要执行的操作序号:'))
    return auth(operate_dic[num - 1][1])

while True:
    res = main(operate_dic1)
    print(res['info'])
    if res['result'] == 'myexit':
        break
    elif res['result']:
        main(operate_dic2)

sk.close()