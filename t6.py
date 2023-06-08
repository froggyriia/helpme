def f1(func):
    def wrapper(*args, ** kwargs):
        print('start')
        func(*args, **kwargs)
        print('finish')
    return wrapper

@f1
def f():
    print('pidor is processing')

f()