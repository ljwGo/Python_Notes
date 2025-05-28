import socketserver
import json
import os
import hashlib
filepath = os.path.join(os.getcwd(), 'info', 'userinfo.txt')
class Auth():
    @staticmethod
    def md5(usr,pwd):
        md5_obj = hashlib.md5(usr.encode())
        md5_obj.update(pwd.encode())
        return md5_obj.hexdigest()

    @classmethod
    def register(cls,opt_dic):
        # 1 监测数据库中是否含有该用户
        with open(filepath,mode='r',encoding='utf-8') as fp:
            for line in fp:
                username = line.split(':')[0]
                if username == opt_dic['user']:
                    return {'result':False,'info':'用户名已存在'}
        with open(filepath,mode='a+',encoding='utf-8') as fp:
            fp.write('%s:%s\n' % (opt_dic['user'],cls.md5(opt_dic['user'],opt_dic['pwd'])))
            return {'result:':False,'info':'注册成功'}

    @classmethod
    def login(cls,opt_dic):
        with open(filepath,mode='r+',encoding='utf-8') as fp:
            for line in fp:
                user,password = line.strip().split(':')
                if user == opt_dic['user'] and password == cls.mad5(opt_dic['user'],opt_dic['pwd']):
                    return {'result:':True,'info':'登录成功'}

    def myexit(self,opt_dic):
        return {'result','myexit'}

    def download(self,):
        pass

class FTPserver(socketserver.BaseRequestHandler):
    def handle(self):
        opt_dic = self.myrecv()
        if hasattr(Auth,opt_dic['operate']):
            func = getattr(Auth,opt_dic['operate'])
            res = func(opt_dic)
            self.mysend(res)

    # 接受数据的方法
    def myrecv(self):
        info = self.request.recv(1024)
        opt_str = info.decode()
        opt_dic = json.loads(opt_str)
        return opt_dic

    def mysend(self,info):
        b_info = json.dumps(info).encode()
        self.request.send(b_info)

server = socketserver.ThreadingTCPServer(('127.0.0.1',9004),FTPserver)
# socketserver.TCPServer.allow_reuse_address = True
# 允许一个端口绑定多个程序，测试时使用
server.serve_forever()