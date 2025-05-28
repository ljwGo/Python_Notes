import socket
import struct
import json
import os

down_dir = os.path.join(os.path.dirname(__file__), 'download')

client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
client.connect(('8.129.38.241',6666))
while 1:
    cmd = input('请输入您要执行的命令:').strip()
    client.send(cmd.encode('utf-8'))

    cmd_res = client.recv(1)
    if cmd_res == b'0':
        info_b = client.recv(1024)
        info_s = info_b.decode('utf-8')
        print(info_s)

    else:
        pack_len = client.recv(4)
        head_length = struct.unpack('i',pack_len)[0]

        head_b = client.recv(head_length)
        head_str = head_b.decode('utf-8')
        head_dic = json.loads(head_str)

        file_size = head_dic.get('file_size')
        file_name = head_dic.get('file_name')

        down_path = os.path.join(down_dir,file_name)
        for k,v in head_dic.items():
            print('{}:   {}'.format(k,v))

        with open(down_path,mode='wb') as f:
            recv_size = 0
            while recv_size < file_size:
                data = client.recv(1024)
                recv_size += len(data)
                f.write(data)
        print('文件下载完毕')