import time


def tell_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print(end_time - start_time)
        return res
    return wrapper
