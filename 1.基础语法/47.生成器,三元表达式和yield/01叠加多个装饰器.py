def deco1(func):
    def wrapper1(*args,**kwargs):
        print('wrapper1执行了')
        res = func(*args,**kwargs)
        return res
    return wrapper1

def deco2(func):
    def wrapper2(*args, **kwargs):
        print('wrapper2执行了')
        res = func(*args, **kwargs)
        return res
    return wrapper2

def deco3(x):
    def outter(func):
        def wrapper3(*args, **kwargs):
            print('wrapper3执行了')
            res = func(*args, **kwargs)
            return res
        return wrapper3
    return outter

# 加载顺序自下而上，执行顺序自外而内
@deco1
@deco2
@deco3(1)
def index(x,y):
    pass

index(2,2)