def login():
    ...
def register():
    pass

operate_list = [login,register]
operate_iter = enumerate(operate_list, 1)
for num,ability in operate_iter:
    print(num,ability)
while True:
    choice = input('请输入您要执行的命令：').strip()
    if choice.isdigit():
        choice = int(choice)
        length = len(operate_list)
        if choice == 0:
            break
        elif 0 < choice <= length:
            operate_list[choice]()
        else:
            print('您输入的命令不存在')
    else:
        print('输入的命令必须是纯数字')