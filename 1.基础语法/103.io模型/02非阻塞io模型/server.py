import socket

server = socket.socket()
server.bind(('127.0.0.1',8080))
server.listen(5)
server.setblocking(False)
server.getblocking()

l = []
w_l = []
while 1:
    try:
        conn,addr = server.accept()
        l.append(conn)

    except BlockingIOError:
        # time.sleep(0.1)
        # print('做其他事情')

        # 收消息
        del_l = []
        for conn in l:
            try:
                data = conn.recv(1024)
                if not data:
                    conn.close()
                    del_l.append(conn)
                    continue
                # conn.send(data.upper())
                w_l.append((conn,data.upper()))
            except BlockingIOError:
                continue
            except ConnectionResetError:
                conn.close()
                continue
                # l.remove(conn) 不能在列表循环期间修改列表的索引
                del_l.append(conn)

        # 发消息
        del_l2 = []
        for item in w_l:
            try:
                conn = item[0]
                data = item[1]
                conn.send(data)
            except BlockingIOError:
                continue
            except ConnectionResetError:
                conn.close()
                del_l2.append(item)
                continue

        # 回收资源
        for item in del_l2:
            w_l.remove(item)

        for conn in del_l:
            l.remove(conn)
