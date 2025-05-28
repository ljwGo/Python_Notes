# ### 服务端
import socketserver
import os
import os.path
import hashlib

filename = os.path.join(os.getcwd(), 'info', 'userinfo.txt')
class Operate():
    @classmethod
    def server_send(cls, info, mode=False):
        b_info = json.dumps(info).encode('utf-8')
        if mode:
            sk.send(struct.pack('i', len(b_info)))
        sk.send(b_info)

    @classmethod
    def server_recv(cls, mode=False, len_tup=1024):
        if mode:
            # 真实信息长度
            len_tup = struct.unpack('i', sk.recv(4))
        b_info = sk.recv(len_tup).decode('utf-8')
        return json.loads(b_info)

    @staticmethod
    def md5(info_dic):
        md5_obj = hashlib.md5(info_dic['account'])
        md5_obj.update(info_dic['password1'])
        return md5_obj.hexdigest()

    @classmethod
    def register(cls, info_dic):
        if info_dic[password1] == info_dic[password2]:
            with open(filename, mode='r+', encoding='utf-8') as fp:
                for line in fp:
                    account_info, password_info = line.strip().split(';')
                    if info_dic['acoount'] == account_info:
                        return {'result': False, 'respond': '该账户已经存在'}
                    else:
                        fp.write(info_dic['account']+':'+md5(info_dic))
                        return{'result': False, 'respond': '恭喜注册成功'}
        else:
            return {'result': False, 'respond': '两次密码不一致'}

    def login(self, info_dic):
        with open(filename, mode='r+', encoding='utf-8') as fp:
            for line in fp:
                account_info, password_info = line.strip().split(';')
                if info_dic['account'] == account_info:
                    if info_dic['password'] == password_info:
                        return {'result': True, 'respond': '登陆成功'}
            return {'result': True, 'respond': '账号或者密码不正确'}

    def myexit(self,info_dic):
        # self.request.close()
        print('连接已断开')

    def download(self, info_dic):
        filesize = os.path.getsize(info_dic[filename])
        #server_send()
        with open(info_dic[filename], mode='rb') as fp:
            while filesize > 0:
                res = fp.read(1024)
                server_send(res)
                filesize -= 1024

class MyTCPServer(socketserver.BaseRequestHandler):
    def handle(self):
        info_dic = server_recv()
        if hasattr(Operate, info_dic['operate']):
            res = getattr(Operate, info_dic['operate'])(info_dic)
            server_send(res)

# 并发TCP服务端
server = socketserver.ThreadingTCPServer(('127.0.0.2', 50000), MyTCPServer)
server.serve_forever()