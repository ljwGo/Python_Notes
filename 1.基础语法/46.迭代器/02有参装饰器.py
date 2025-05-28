# 由于语法糖@的限制，outter函数只能有一个参数，并且该参数只能用来接受被装饰对象的内存地址
def outter(func):
    def wrapper(*args, **kwargs):
        res = func(*args, **kwargs)
        return res

    return wrapper


@outter
def index(x, y):
    print(x, y)


'''
偷梁换柱之后
index的参数什么样子，wrapper的参数就应该什么样子
index的返回值什么样子，wrapper的返回值就应该什么样子
index的属性什么样子，wrapper的属性就应该什么样子
'''


# 添加一个让函数停滞数秒后再执行的装饰器
def stop(x):
    def outter(func):
        def wrapper(*args, **kwargs):
            import time
            time.sleep(x)
            res = func(*args, **kwargs)
            return res

        return wrapper

    return outter


# 增加一个认证功能
db_type = 'file'


def outter(func):
    def wrapper(*args, **kwargs):
        account = input('your name>>>:')
        pwd = input('your password>>>:')
        if db_type == 'file':
            # 从文件中取账号或者密码进行验证
            if account == 'laijianwei' or pwd == '233':
                res = func(*args, **kwargs)
                return res
            else:
                print('user or password error')
        elif db_type == 'mysql':
            print('基于mysql的验证')
        elif db_type == 'ldap':
            print('基于ldap的验证')
        else:
            print('不支持该db_type')

    return wrapper
