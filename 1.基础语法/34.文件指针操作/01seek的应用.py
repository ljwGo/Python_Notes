import time
file = input('请输入您要检测的文件名>>>:')
with open('{}'.format(file), mode='rb') as f:
    f.seek(0,2)
    while True:
        res = f.readline()
        time.sleep(0.3)
        if res:
            print(res.decode('utf-8'),end='')
